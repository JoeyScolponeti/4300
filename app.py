import streamlit as st
from MANUAL import reconstruct
from MKTBAPI import read
import pandas as pd
import csv


st.header('Pro Mario Kart Wii Database')

df = st.file_uploader(label= 'Upload File', type=['txt'])

if df:
    file_bytes = df.read()
    file_data = file_bytes.decode("utf-8").split('\n')
    matches, num = read(file_data)
    st.write(matches[0])


