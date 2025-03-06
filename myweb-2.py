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


st.write(revised_data)