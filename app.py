import streamlit as st
import pandas as pd
import altair as alt
#make a title for this demo using emojis
st.title('DevOps Outlook')

st.title("Service Health")

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