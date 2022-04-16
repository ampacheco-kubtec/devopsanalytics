import streamlit as st
import pandas as pd
import altair as alt
#make a title for this demo using emojis

#
# Set of useful functions
#

#######################################################################################################################
def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df
#######################################################################################################################

st.title('DevOps Outlook')

# APP connected to CognitiveService

# First Panel
st.title("Service Health")

# Service Health Raw Data
sh_rawdata="https://raw.githubusercontent.com/ampacheco-kubtec/devopsanalytics/main/data/services-health.csv"

st.write(sh_rawdata)

@st.cache
df = read_csv(sh_rawdata)

st.write(df)


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