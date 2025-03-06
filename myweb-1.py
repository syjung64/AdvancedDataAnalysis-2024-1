# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import streamlit as st

st.write("""
         # Data Analysis Dash Board
         Developer Survey by sukyong Jung
         """)
         
raw_data = pd.read_csv('survey_results_public.csv')
revised_data = raw_data[['Age', 'Country', 'LanguageHaveWorkedWith', 'LearnCode']]

kor_data = revised_data.query('Country == "South Korea"')

st.write(kor_data)
