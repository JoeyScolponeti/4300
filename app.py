import streamlit as st
from MANUAL import reconstruct
import pandas as pd



st.header('Pro Mario Kart Wii Database')

df = st.file_uploader(label= 'Upload Season', type=['csv'])

if df:
    df = pd.read_csv(df)
    output = reconstruct(df)
    st.write(output['tracks'])


