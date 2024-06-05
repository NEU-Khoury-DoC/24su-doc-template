import logging

import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger()

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Activist, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Posts',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/10_View_Posts.py')

if st.button('Create a New Post',
              type='primary',
              use_container_width=True):
    st.switch_page('pages/11_New_Post.py')

if st.button('Update or Delete a Post',
              type='primary',
              use_container_width=True):
    st.switch_page('pages/12_Update_Delete_Post.py')

if st.button('View Protests',
              type='primary',
              use_container_width=True):
    st.switch_page('pages/20_View_Protests.py')

if st.button('Create a New Protest',
              type='primary',
              use_container_width=True):
    st.switch_page('pages/21_New_Protest.py')

if st.button('Update or Delete a Protest',
              type='primary',
              use_container_width=True):
    st.switch_page('pages/22_Update_Delete_Protest.py')