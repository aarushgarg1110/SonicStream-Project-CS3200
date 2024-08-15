# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Role of listener ------------------------
def ListenerHomeNav():
    st.sidebar.page_link("pages/00_Listener_Home.py", label="Listener Home", icon='👤')
    st.sidebar.page_link("pages/01_Song_Finder.py", label="Song Finder", icon='🎶')
    st.sidebar.page_link("pages/02_Follow_Artist.py", label="Follow An Artist", icon='👩‍🎤')
    st.sidebar.page_link("pages/03_Review_Song.py", label="Review A Song", icon='✍️')
    st.sidebar.page_link("pages/04_Common_Songs.py", label="Find Common Songs W/ Friends", icon='🫂')

def MapDemoNav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Map Demo", icon='🗺️')

## ------------------------ Role of Artist ------------------------

def ArtistHomeNav():
    st.sidebar.page_link("pages/10_Artist_Home.py", label="Artist Home", icon='👤')
    st.sidebar.page_link("pages/11_Song_Incomes.py", label="Income From Songs", icon='💸')
    st.sidebar.page_link("pages/12_Upload_Song.py", label="Upload A Song", icon='🎶')
    st.sidebar.page_link("pages/13_Popular_Songs.py", label="View Most Popular Songs", icon='🔥')
    st.sidebar.page_link("pages/14_Promote_Concert.py", label="Promote A Concert", icon='🥁')

def ApiTestNav():
    st.sidebar.page_link("pages/12_API_Test.py", label="Test the API", icon='🛜')

def PredictionNav():
    st.sidebar.page_link("pages/11_Prediction.py", label="Regression Prediction", icon='📈')

def ClassificationNav():
    st.sidebar.page_link("pages/13_Classification.py", label="Classification Demo", icon='🌺')

#### ------------------------ Marketing Admin Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon='🖥️')
    st.sidebar.page_link("pages/21_Monitor_Ads.py", label='Monitor All Advertisements', icon='🧑‍💻')
    st.sidebar.page_link("pages/22_Update_Ads.py", label='Update Status of an Ad', icon='📝')
    st.sidebar.page_link("pages/23_Company_Revenue.py", label='View Company Revenue', icon='💸')
    st.sidebar.page_link("pages/24_Top10_Artists.py", label='Hottest Artists of The Month', icon='🔥')
    st.sidebar.page_link("pages/25_Ban_User.py", label='Ban A User', icon='❌')


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width = 250)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
        
    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state['role'] == 'listener':
            ListenerHomeNav()
            MapDemoNav()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state['role'] == 'artist':
            ArtistHomeNav()
            PredictionNav()
            ApiTestNav() 
            ClassificationNav()
        
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'administrator':
            AdminPageNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

