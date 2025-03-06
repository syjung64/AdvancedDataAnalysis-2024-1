# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import streamlit as st

st.write("""
         # Data Analysis Dash Board
         Developer Survey
         """)
         
raw_data = pd.read_csv('survey_results_public.csv')
revised_data = raw_data[['Age', 'Country', 'LanguageHaveWorkedWith', 'LearnCode']]


age = revised_data['Age'].unique().tolist()
st.sidebar.title('Age')
select_ages = st.sidebar.selectbox(
    '나이를 선택하세요', age
)

tmp_df = revised_data[revised_data['Age']==select_ages]
st.write(tmp_df)