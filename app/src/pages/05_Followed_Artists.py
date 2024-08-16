import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import matplotlib.pyplot as plt
import requests
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Select artist')
user = st.session_state['username']
# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['username']}.")

# Make a GET request to the API
api_url_artists = f'http://web-api:4000/l/listeners/Followedartists/{user}'
response_artists = requests.get(api_url_artists)

# Check if the request was successful
if response_artists.status_code == 200:
    # Extract the data from the JSON response
    artist_data = response_artists.json()

    # Extract artist names from the fetched data
    artist_names = [artist['name'] for artist in artist_data]

    # Populate the selectbox with artist names
    selected_artist = st.selectbox("Select an Artist", artist_names, index=None, placeholder="Select artist...")

    # Add a button to confirm the selection
    if st.button("Confirm Selection"):
        if selected_artist:
            st.write(f"You selected: {selected_artist}")

            # Fetch the artist's songs
            api_url_songs = f'http://web-api:4000/l/artists/songs/{selected_artist}'
            response_songs = requests.get(api_url_songs)

            if response_songs.status_code == 200:
                songs = response_songs.json()
                if songs:
                    st.write(f"### Songs by {selected_artist}:")
                    for song in songs:
                        st.write(f"- {song['title']}")
                else:
                    st.write(f"No songs found for {selected_artist}.")
            else:
                st.error(f"Failed to fetch songs for {selected_artist}. Status Code: {response_songs.status_code}")

            # Fetch the artist's upcoming concerts
            api_url_concerts = f'http://web-api:4000/l/artists/concerts/{selected_artist}'
            response_concerts = requests.get(api_url_concerts)

            if response_concerts.status_code == 200:
                concerts = response_concerts.json()
                if concerts:
                    st.write(f"### Upcoming Concerts for {selected_artist}:")
                    for concert in concerts:
                        st.write(f"- Venue: {concert['venue']}, Date: {concert['event_date']}")
                else:
                    st.write(f"No upcoming concerts found for {selected_artist}.")
            else:
                st.error(f"Failed to fetch concerts for {selected_artist}. Status Code: {response_concerts.status_code}")
        else:
            st.write("Please select an artist.")

else:
    st.error("Failed to fetch artists. Please try again later.")