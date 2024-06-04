import logging
logger = logging.getLogger()

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome PR Specialist, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')