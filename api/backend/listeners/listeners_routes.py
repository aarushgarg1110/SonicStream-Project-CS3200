from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

listeners = Blueprint('listeners', __name__)

# find songs that match a specific mood or keyword
@listeners.route('/listeners/song/<keyword>', methods=['GET'])
def get_songs_on_mood(keyword):
    keyword = request.view_args['keyword']

    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Use parameterized query to avoid SQL injection
    query = '''
        SELECT s.title, s.album, s.genre, s.duration s.release_date
        FROM song s
        JOIN review r ON s.id = r.song_id
        WHERE r.text LIKE %s
    '''

    # Execute the query with the keyword parameter
    cursor.execute(query, ('%' + keyword + '%'))

    # grab the column headers from the returned data
    # column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    # json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    # for row in theData:
    #     json_data.append(dict(zip(column_headers, row)))

    return jsonify(theData)

# follow a specific artist
# @listeners

# make a review on a song

# edit a review on a song

# delete a review from a song

# retrieve all songs that a user has in common with their friend