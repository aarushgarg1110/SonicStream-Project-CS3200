import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    SonicStream is a music streaming platform that allows users to:
      discover new music, 
      organize their favorite tunes into separate playlists, 
      and stay updated on upcoming tours\shows of their favorite artists. 
      
    Not only can users follow their favorite artists, but they can also follow other users to see which songs 
    they mutually listen to. To make the listening experience more personalized, users can like/rate certain 
    songs to see similar songs in their recommended feed later on. They can also leave comments on the songs 
    for the community to see. 
    
    As an artist on SonicStream, you have the ability to upload all of your singles or albums 
    for all users to listen to. As your songs gain popularity from users on the platform, you’ll start 
    accumulating revenue based on the amount of listens each song obtains. Artists have access to detailed 
    analytics of their listeners, allowing them to better understand their audience and improve promotional 
    techniques. SonicStream allows artists to stay connected with their fans by keeping them posted on 
    upcoming tours/shows. 

    The efficiency of SonicStream’s music services would not be possible without our marketing administrators. 
    They play a crucial role in presenting users with personalized content and assisting artists with promotions 
    and profits. 

    """
        )
