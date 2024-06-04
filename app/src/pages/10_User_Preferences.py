import logging
logger = logging.getLogger()
import requests
import pandas as pd

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Profile Information')
st.divider()
import streamlit as st
st.markdown(f"<p style='font-size:24px;'>First Name: {st.session_state['first_name']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size:24px;'>Last Name: {st.session_state['last_name']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size:24px;'>Job Description: {st.session_state['role']}</p>", unsafe_allow_html=True)

st.write('### User Preferences')
st.divider()

st.date_input("Preferred Timeline")

df = pd.read_csv('app/src/pages/Countries_Data.csv')

country_names = [country['name'] for country in df]

country_names.sort()
st.selectbox("News Subject Country", country_names)
st.selectbox("News Source Country", country_names)

st.date_input("Preferred Timeline")







