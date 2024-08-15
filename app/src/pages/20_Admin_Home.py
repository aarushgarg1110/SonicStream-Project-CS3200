import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Home Page')

if st.button('Monitor Ads',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Monitor_Ads.py')

if st.button('Update the Status of an Ad',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Update_Ads.py')

if st.button('Fetch the 10 most recently liked artists',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/24_Top10_Artists.py')

if st.button('See how much money the company has made from songs',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Company_Revenue.py')

if st.button('Ban a User',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/25_Ban_User.py')