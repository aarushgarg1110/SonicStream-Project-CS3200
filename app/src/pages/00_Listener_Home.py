import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Music Listener, {st.session_state['username']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Find songs based on your mood', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Song_Finder.py')

if st.button('Follow a new artist', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Follow_Artist.py')

if st.button('Leave a review on a song', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/03_Review_Song.py')

if st.button('See what songs you and your friends have in common', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/04_Common_Songs.py')

if st.button('View info about your favorite artists',
             type = 'primary',
             use_container_width=True):
  st.switch_page('pages/05_Followed_Artists.py')