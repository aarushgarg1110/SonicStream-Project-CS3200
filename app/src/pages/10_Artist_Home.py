import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Artist, {st.session_state['firstname']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View your income from all your songs', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Song_Incomes.py')

if st.button('Upload a song', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Upload_Song.py')

if st.button("View your most popular songs",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Popular_Songs.py')

if st.button("Promote a Concert",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Promote_Concert.py')