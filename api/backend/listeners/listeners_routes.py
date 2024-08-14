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
# follow a specific artist
@listeners.route('/listeners/artists', methods=['POST'])
def follow_artists():
    the_data = request.json
    current_app.logger.info(the_data)

    listener_id = the_data['listener_id']
    artist_id = the_data['artist_id']
    
    query = '''
        INSERT INTO listener_artist(listener_id, artist_id)
        VALUES (%s, %s)
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (listener_id, artist_id))
    db.get_db().commit()

    return 'Success'

# make a review on a song
@listeners.route('/reviews', methods=['POST'])
def make_review():
    the_data = request.json
    current_app.logger.info(the_data)

    listener_id = the_data['listener_id']
    song_id = the_data['song_id']
    review_num = the_data['review_num']
    text = the_data['text']

    query = ''''
    INSERT INTO review(song_id, review_num, listener_id, text)
    VALUES (%s, %s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (song_id, review_num, listener_id, text))
    db.get_db().commit()

    return 'Success'

# edit a review on a song

# delete a review from a song

# retrieve all songs that a user has in common with their friend
@listeners.route('/songs', methods=['GET'])
def common_songs():
    current_app.logger.info('listeners_routes.py: GET /songs')

    username = request.args.get('username')
    friend_username = request.args.get('friend_username')

    query = '''
    SELECT s.title AS common_songs_with_friend
    FROM
    (
        SELECT l.id AS userId, lf.id AS friendID
        FROM listener l
            JOIN friends f ON l.id = f.userID
            JOIN listener lf ON lf.id = f.friendID
        WHERE l.username = '%s'
        AND lf.username = '%s'
    ) AS infoID
    JOIN playlist_song ps1 ON ps1.listenerID = infoID.userID
    JOIN playlist_song ps2 ON ps2.listenerID = infoID.friendID
    JOIN song s ON ps1.song_id = s.id
    WHERE ps1.song_id = ps2.song_id;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (username, friend_username))

    common_songs = cursor.fetchall()
    the_response = make_response(common_songs)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


