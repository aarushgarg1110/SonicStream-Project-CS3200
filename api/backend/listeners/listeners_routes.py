from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

listeners = Blueprint('listeners', __name__)

# Convert timedelta from sql to minutes and seconds
def serialize_timedelta(td):
    total_seconds = int(td.total_seconds())
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes:02}:{seconds:02}"

# find songs that match a specific mood or keyword
# @listeners.route('/listeners/songs', methods=['GET'])
# def get_songs():
#     current_app.logger.info('songs_routes.py: GET /songs')
#     cursor = db.get_db().cursor()
#     query = '''
#         SELECT s.title, s.album, s.genre, s.duration, s.release_date 
#         FROM song s JOIN review r ON s.id = r.song_id
#         WHERE r.text LIKE '%married%'
#     '''
#     cursor.execute(query)
#     theData = cursor.fetchall() 
#     the_response = make_response(theData)
#     the_response.status_code = 200
#     the_response.mimetype = 'application/json'
#     return the_response

# follow a specific artist

# make a review on a song

# edit a review on a song

# delete a review from a song

# retrieve all songs that a user has in common with their friend