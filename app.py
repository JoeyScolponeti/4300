import streamlit as st


st.header('Pro Mario Kart Wii Database')

df = st.file_uploader(label= 'Upload Season', type=['csv'])


