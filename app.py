import json
import streamlit as st
from MANUAL import reconstruct
from MKTBAPI import read
import pandas as pd
import csv
import boto3

s3_client = boto3.client('s3')

bucket = "4300-final-bucket"

st.header('Pro Mario Kart Wii Database')

df = st.file_uploader(label= 'Upload File', type=['txt'])

count = 0

if df:
    count += 1
    file_bytes = df.read()
    file_data = file_bytes.decode("utf-8").split('\n')
    matches, num = read(file_data)
    st.write(matches[0])

    new_file = 'Season' + str(count)

    with open (new_file, 'w') as f:
        f.write(file_data)

    s3_client.upload_file(new_file + '.txt', bucket, new_file)




