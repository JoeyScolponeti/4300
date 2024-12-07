import json
import streamlit as st
from MANUAL import reconstruct
from MKTBAPI import read
import pandas as pd
import csv
import boto3

s3_client = boto3.client('s3')

bucket = "mkw-bucket"

st.header('Pro Mario Kart Wii Database')

df = st.file_uploader(label= 'Upload File', type=['txt'])

if df:
    file_bytes = df.read()
    file_data = file_bytes.decode("utf-8").split('\n')
    matches, num = read(file_data)
    st.write(matches[0])

    new_file = file_data[0][15:17] + '.txt'

    with open (new_file, 'w') as f:
        for match in matches:
            df = match.match_df()
            new_file.write(df)

    s3_client.upload_file(new_file, bucket, new_file)




