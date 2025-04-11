import numpy as np
import streamlit as st
import pandas as pd
import json

st.title("QC Entry")

with st.container(border=True):
    titleinput = st.text_input("Title")
    episodenumber, episodename, runtime = st.columns([1,3,1])
    with runtime:
        runtimeinput = st.time_input("Runtime", value=None)
    with episodename:
        epnameinput = st.text_input("Episode Name", value=None)
    with episodenumber:
        epnuminput = st.text_input("Ep./Prod. Number", value=None)

df = pd.DataFrame({
    'Timecode': [""],
    'Issue': [""],
    'A/V/F': [""],
    'Scale': [""],
})

df['Timecode'] = df['Timecode'].astype(str)
df['Issue'] = df['Issue'].astype(str)
df['A/V/F'] = df['A/V/F'].astype(str)
df['Scale'] = df['Scale'].astype(str)



columnconfig = {
    'Timecode': st.column_config.TextColumn(width='small'),
    'Issue': st.column_config.TextColumn(width='medium'),
    'A/V/F': st.column_config.TextColumn(width='small'),
    'Scale': st.column_config.TextColumn(width='small')
}

with st.container(border=True):
    data = st.data_editor(df,hide_index=True,num_rows="dynamic",column_config=columnconfig)

with st.container(border=False):
    videoqc, spqc = st.columns(2, border=True)
    with videoqc:
        videoinput = st.selectbox("Video & Audio:", ["Pass", "Review", "Fail"])
    with spqc:
        spinput = st.selectbox("S&P", ["Pass", "Fail"])


qcdata = {
    'title': titleinput,
    'episode_info': {
        'episode_number': epnuminput,
        'episode_name': epnameinput,
        'runtime': str(runtimeinput)
    },
    'dataframe': {
        'Timecode': data['Timecode'].tolist(),
        'Issue': data['Issue'].tolist(),
        'A/V/F': data['A/V/F'].tolist(),
    },
    'video_audio_quality': videoinput,
    'sp_quality': spinput
}

#st.write(f'qcdata: {qcdata}')

#qcdatajson = 'qcdata.json'

#with open(qcdatajson,'w') as file:
    #json.dump(qcdata,file,indent=4)

#with st.container(border=True):
   # if st.button("Save"):
      #  qcdatajson.append(new_entry)
