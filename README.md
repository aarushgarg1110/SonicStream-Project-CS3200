# Summer 2024 CS 3200 SuperSonics - SonicStream

## Presentation Video
[https://drive.google.com/file/d/1y7M5kCStTMEVUlAVC-fExcxfUiLyo4BG/view?usp=sharing](url)

## About

This is a project that utilizes Flask and Streamlit to work with a MySQL database.

Team Name: SuperSonics

Team Members:
Aarush Garg,
Robert Doss,
William Sartorio,
Ryan Brueckner,
Yifan Xing

SonicStream is a music streaming platform that allows users to discover new music, organize their favorite tunes into separate playlists, and stay updated on upcoming tours\shows of their favorite artists. Not only can users follow their favorite artists, but they can also follow other users to see which songs they mutually listen to. To make the listening experience more personalized, users can like/rate certain songs to see similar songs in their recommended feed later on. They can also leave comments on the songs for the community to see. As an artist on SonicStream, you have the ability to upload all of your singles or albums for all users to listen to. As your songs gain popularity from users on the platform, you’ll start accumulating revenue based on the amount of listens each song obtains. Artists have access to detailed analytics of their listeners, allowing them to better understand their audience and improve promotional techniques. SonicStream allows artists to stay connected with their fans by keeping them posted on upcoming tours/shows. 
The efficiency of SonicStream’s music services would not be possible without our marketing administrators. They play a crucial role in presenting users with personalized content and assisting artists with promotions and profits. 

--------------
Features
--------------
A Music Listener can:
- find a song based on their mood
- follow an artist
- see their followed artists and their associated songs and upcoming concerts
- Leave a review on a song
- Find songs in common with their friends on SonicStream

An Artist can:
- View their income generated from songs
- Upload a song
- View their most popular songs on the app in order
- Promote a concert

A Marketing Admin for SonicStream:
- Monitor all advertisement campaigns on the app (past and present)
- Update the status of an ad
- View company revenue generated from all the songs/ads on the app
- View the app's hottest artists over any period of time within a year
- Ban a user if needed
 

## Current Project Components

Currently, there are three major components:
- Streamlit App (in the `./app` directory)
- Flask REST api (in the `./api` directory)
- MySQL setup files (in the `./database-files` directory)

## Getting Started for Personal Exploration
1. Clone the repo to your computer. 
1. Set up the `.env` file in the `api` folder based on the `.env.template` file.
2. Run pip install -r requirements.txt with [https://www.dropbox.com/scl/fi/sdsugwz51bx4135ph2k7y/requirements.txt?rlkey=dqcuzugbt0rp0bs1lafxjrswd&dl=0](url)
3. Run pip install streamlit
4. In the .env file, type in 'sonic_stream' for the DB_NAME and set any password for MYSQL_ROOT_PASSWORD.
5. Open a terminal in the project folder you cloned into, in the terminal write 'docker --version' to check you are connected to docker.
6. then type in 'docker compose up -d' to start/compose the containers
7. Go to DataGrip, Create a new MySQL data source
8. In the properties, give it any name
9. Make username root
10. Make password the password you set in the .env file
11. Change port to 3200
12. Test your connection to see if it succeeds
13. Press OK
14. Open up localhost:8501 or run python -m streamlit hello to see our project run

 
