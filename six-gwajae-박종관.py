import pandas as pd
import streamlit as st
import plotly.express as px
from functools import reduce

st.write("""
# Data Analysis Dash Board 
> programmed by 박종관, Modified by 정석용
""")

raw_data = pd.read_csv('owid-covid-data.csv')
revised_data = raw_data[['iso_code', 'location', 'date', 'new_cases', 'population']].copy()
revised_data['date'] = pd.to_datetime(revised_data['date'])
revised_data['year'] = revised_data['date'].dt.year
revised_data['month'] = revised_data['date'].dt.month

# 연도 데이터 추출하여 리스트로 저장
year = revised_data['year'].unique().tolist()
# 국가 이름 추출하여 리스트로 저장
countries = revised_data['location'].unique().tolist()


st.sidebar.title('Sidebar')

# multi selelct
select_country = st.sidebar.multiselect('나라를 선택하시오. 복수 선택 가능', countries)

# radio box
select_year = st.sidebar.radio('연도를 선택하시오', year, horizontal=True)

# slide bar 생성
select_range = st.sidebar.slider("원하는 월을 선택하시오", min_value=1, max_value=12, value=(1, 12))
start_month, end_month = select_range

# filter start button
start = st.sidebar.button('filter apply')

if start:
    tmp_df = revised_data[revised_data['year'] == select_year]
    
    country_df_list = []
    country_list = []
    for i in select_country :
        globals()[f'{i}_total'] = tmp_df.query(f'(location == "{i}") & (month >= @start_month) & (month <= @end_month)')[['date', 'new_cases']]
        globals()[f'{i}_total'] = globals()[f'{i}_total'][['date', 'new_cases']].rename(columns={'new_cases': i})
        country_df_list.append(globals()[f'{i}_total'])
        country_list.append(i)
                  
    final_df = reduce(lambda x,y: pd.merge(x,y, on='date', how='outer'), country_df_list)                  

    fig = px.line(
        final_df,
        x='date',
        y=country_list,
        title='나라별 신규 확진자 수'
    )
    st.plotly_chart(fig)

    st.sidebar.success('filter apply success')
    st.balloons()