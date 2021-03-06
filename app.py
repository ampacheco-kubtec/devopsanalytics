import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
#make a title for this demo using emojis

#
# Set of useful functions
#

st.title('DevOps Outlook')

# APP connected to CognitiveService

# First Panel
st.title("Service Health")

# Service Health Raw Data
sh_rawdata="https://raw.githubusercontent.com/ampacheco-kubtec/devopsanalytics/main/data/services-health.csv"

st.write(sh_rawdata)

@st.cache
#######################################################################################################################
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df
#######################################################################################################################
df = read_csv(sh_rawdata)

st.write(df)
st.map(df)

st.dataframe(df)

na_df = df[df['Data Center'].isin(['North America'])]
sa_df = df[df['Data Center'].isin(['South America'])]
eu_df = df[df['Data Center'].isin(['East Europe'])]

st.dataframe(na_df)
st.dataframe(sa_df)
st.dataframe(eu_df)

##
## Chamullo
##

# TODO:
# Filtrar df 

row1_1, row1_2, row1_3 = st.columns(3)

with row1_1:
    ''' ### North America '''  
    ''' #### # Users by Service '''    
    chart_data = na_df.filter(items=['S1','S2','S3','S4','S5']).transpose()
    st.bar_chart(chart_data)  

with row1_2:
    ''' ### South America '''  
    ''' #### # Users by Service '''  
    chart_data = sa_df.filter(items=['S1','S2','S3','S4','S5']).transpose()
    st.bar_chart(chart_data)  

with row1_3:
    ''' ### Europe '''  
    ''' #### # Users by Service '''  
    chart_data = eu_df.filter(items=['S1','S2','S3','S4','S5']).transpose()
    st.bar_chart(chart_data)  

# Others Metric
row2_1, row2_2 = st.columns([2,2])

with row2_1:
    st.title("Métrica 1")

with row2_2:
    st.title("Métrica 2")

row3_1, row3_2 = st.columns([2,2])

with row3_1:
    st.title("Métrica 3")

with row3_2:
    st.title("Métrica 4")