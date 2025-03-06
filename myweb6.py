# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import streamlit as st
import plotly.express as px

st.write("""
         # Data Analysis Dash Board
         Developer Survey
         """)
         
raw_data = pd.read_csv('survey_results_public.csv')
revised_data = raw_data[['Age', 'Country', 'LanguageHaveWorkedWith', 'LearnCode']]


age = revised_data['Age'].unique().tolist()

st.sidebar.title('Age')
select_multi_ages = st.sidebar.multiselect(
    '나이를 선택하세요. 복수 선택 가능', age
)

radio_select = st.sidebar.radio(
    "나라를 선택하시오.",
    ['South Korea', 'Canada', 'Sweden', 'India'],
    horizontal=True
)

start_button = st.sidebar.button(
    'filter apply'
)

if start_button:
    tmp_df = revised_data[revised_data['Age'].isin(select_multi_ages)]
    tmp_df = revised_data[revised_data['Country'] == radio_select]
    st.write(tmp_df)
    
    learn = tmp_df['LearnCode']
    learn = learn.str.split(';').explode()
    data = learn.groupby(learn).size().head(5)
    fig = px.pie(
        data,
        values = data.values,
        names = data.index,
        title='fig. How to learn'
    )
    st.plotly_chart(fig)
    
    st.sidebar.success('filter Applied')
    st.balloons()