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
select_multi_ages = st.sidebar.multiselect(
    '나이를 선택하세요. 복수 선택 가능', age
)

tmp_df = revised_data[revised_data['Age'].isin(select_multi_ages)]
st.write(tmp_df)