# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:12:37 2023

@author: Jay
"""

import pandas as pd
import streamlit as st
import requests
import plotly.express as px

# sidebar 만들기
st.sidebar.title('주식시세 Dash Board')

# multi selelct
stock_code = {'삼성전자':'005930', '하이닉스':'000660', '크래프톤':'259960', '주성엔지니어링':'036930'}

stocks = list(stock_code.keys())

selected_tab = st.tabs(stocks)

for list_loop in range(len(stocks)):
    with selected_tab[list_loop]:
        s_code = stock_code[stocks[list_loop]]
        st.write(s_code)
        
        # 요청 헤더 정보 설정
        my_headers = {'user-agent':'Mozilla/5.0'}

        #stock_url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page='
        stock_url = 'https://finance.naver.com/item/sise_day.naver?code='+s_code+'&page='


        # 데이터(상성전자 일일 주가 페이지)를 축적할 데이터프레임 생성
        all_tables = pd.DataFrame()

        # 10 페이지 읽어오기 (100일치 주식 데이터 일어오기)
        for page_number in range(1, 11):
            # 페이지 번호 추가한 주소 완성
            full_url = stock_url + str(page_number)
            
            #주소 확인하기
            print(f'{page_number}번째 페이지 읽어오기({full_url})' )
            
            # HTTP 요청 전송 후 응답 받아오기
            page = requests.get(full_url, headers=my_headers)
                  
            # 테이블 추출
            table = pd.read_html(page.text)[0]
                  
            # 수행할 내용
            print(f'전체 {len(all_tables.index)} 줄에 {len(table.index)} 줄 추가')
                  
            # 데이터 축적용 데이터프레임에 테이블 추가
            all_tables = pd.concat([all_tables, table])
            
        # 결측치 제거
        all_tables.dropna(inplace=True)

        all_tables.sort_values(by='날짜', inplace=True)


        # 전체 숫자 데이터 선 그래프 그리기
        all_tables.plot.line()
        fig = px.line(
            all_tables,
            x='날짜',
            y='종가',
            title=stocks[list_loop]
        )
        st.plotly_chart(fig)