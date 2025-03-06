# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:43:57 2023

@author: Jay
"""

import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium
from folium.plugins import HeatMap

# 서울 지하철 시간대별 승하차 인원 데이터 읽어오기
data = pd.read_csv('seoul-metro-2021.logs.csv')
data['hour'] = pd.to_datetime(data['timestamp']).dt.hour

# 서울 지하철 역 정보 데이터 읽어오기
station_info = pd.read_csv('seoul-metro-station-info.csv')


# sidebar 만들기
st.sidebar.title('서울 지하철 승하차 혼잡도')

# radio box
select = st.sidebar.radio('승하차 선택', ['승차', '하차'], horizontal=True)

# slide bar 생성
select_range = st.sidebar.slider("원하는 시간을 선택하시오", min_value=0, max_value=24, value=(0, 24))
start_hour, end_hour = select_range

# filter start button
start = st.sidebar.button('filter apply')

# 승차인원 분석 시간대 적용
hour_data = data.query('(hour > @start_hour) & (hour < @end_hour)')

# 역 기준으로 승차인원 합치기
# 숫자 타입이 아닌 timestamp는 사라짐
station_sum = hour_data.groupby('station_code')[['people_in', 'people_out']].sum()

# 필요한 변수만 고르기
station_info = station_info[['station.code', 'geo.latitude', 'geo.longitude', 'station.name']]

# 승하차 데이터와 색인 맞추기
station_info = station_info.set_index('station.code')

# 승하차 인원 데이터와 지하철역 정보 데이터 합치기
# 색인을 기준으로 데이터 합치기 : join()
joined_data = station_sum.join(station_info)
    
# 승차 인원 시각화 (승차용 서울지도 만들기)
seoul = folium.Map(location=[37.55, 126.98], zoom_start = 12)

if start:
    if select == '승차' :
        HeatMap(data=joined_data[['geo.latitude', 'geo.longitude','people_in']]).add_to(seoul)
        st.write(joined_data.sort_values(by='people_in', ascending=False).head(10)[['people_in', 'station.name']])

    elif select == '하차' :
        HeatMap(data=joined_data[['geo.latitude', 'geo.longitude','people_out']]).add_to(seoul)
        st.write(joined_data.sort_values(by='people_out', ascending=False).head(10)[['people_out', 'station.name']])
    else :
        st.write("ELSE")

    st_folium(seoul, returned_objects=[])