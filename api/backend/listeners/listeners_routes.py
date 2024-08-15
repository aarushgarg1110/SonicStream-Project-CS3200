from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

listeners = Blueprint('listeners', __name__)

# find songs that match a specific mood or keyword
@listeners.route('/listeners/song/<keyword>', methods=['GET'])
def get_songs_on_mood(keyword):
    keyword = request.view_args['keyword']

    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Use parameterized query to avoid SQL injection
    query = '''
        SELECT s.title, s.album, s.genre
        FROM song s
        JOIN review r ON s.id = r.song_id
        WHERE r.text LIKE %s
    '''

    # Execute the query with the keyword parameter
    cursor.execute(query, ('%' + keyword + '%'))

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    return jsonify(theData)

# follow a specific artist
@listeners.route('/listeners/artists/<username>/<artistname>', methods=['POST'])
def follow_artists(username, artistname):
    try:
        query = '''
            INSERT INTO listener_artist(listener_id, artist_id)
            SELECT l.id, a.id
            FROM listener l, artist a
            WHERE l.username = %s AND a.name = %s;
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(query, (username, artistname))
        db.get_db().commit()
        
        # Check if any rows were actually inserted
        if cursor.rowcount == 0:
            return 'Artist not found or already followed', 400
        
        return 'Success', 200

    except Exception as e:
        # Log the exact error for debugging purposes
        current_app.logger.error(f"Error following artist: {str(e)}")
        return 'Internal Server Error', 500

# get list of all songs - for use in 03_review_song
@listeners.route('/listeners/get_songs', methods=['GET'])
def get_songs():
    cursor = db.get_db().cursor()
    query = '''
    SELECT title
    FROM song
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    return jsonify(theData)

# make a review on a song
@listeners.route('/reviews/<text>/<username>/<song>', methods=['POST'])
def make_review(text, username, song):

    query = '''
    INSERT INTO review(song_id, listener_id, text)
    SELECT s.id, l.id, %s
    FROM listener l, song s
    WHERE l.username = %s AND s.title = %s
    '''
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (text, username, song))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return 'Song not found', 400
        
        return 'Success', 200
    
    except Exception as e:
        current_app.logger.error(f'Error while inserting review: {str(e)}')
        return 'Failed to upload review', 500


# edit a review on a song

# delete a review from a song

# retrieve all of [userID, friendID, username, friend_username] for a user
# code to extract friend username from this is in 04_common_songs
@listeners.route('/listeners/friends/<username>', methods=['GET'])
def get_friends(username):
    current_app.logger.info('listeners_routes.py: GET /friends')

    username = request.view_args['username']

    query = '''
    SELECT l.id AS userID, lf.id AS friendID, l.username AS listener1, lf.username AS listener2
    FROM listener l
         JOIN friends f ON l.id = f.userID
         JOIN listener lf ON lf.id = f.friendID
        WHERE l.username = %s
        OR lf.username = %s;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (username, username))

    friends = cursor.fetchall()
    return jsonify(friends)

# retrieve all songs that a user has in common with their friend
@listeners.route('/listeners/songs/<username>/<friend>', methods=['GET'])
def common_songs(username, friend):
    current_app.logger.info('listeners_routes.py: GET /songs')

    username = request.view_args['username']
    friend = request.view_args['friend']

    query = '''
    SELECT s.title, s.album, a.name
    FROM
    (
        SELECT l.id AS userId, lf.id AS friendID
        FROM listener l
            JOIN friends f ON l.id = f.userID
            JOIN listener lf ON lf.id = f.friendID
        WHERE l.username = %s
        AND lf.username = %s
    ) AS infoID
    JOIN playlist_song ps1 ON ps1.listenerID = infoID.userID
    JOIN playlist_song ps2 ON ps2.listenerID = infoID.friendID
    JOIN song s ON ps1.song_id = s.id
    JOIN artist_song asg ON s.id = asg.song_id
    JOIN artist a ON asg.artist_id = a.id
    WHERE ps1.song_id = ps2.song_id;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (username, friend))

    common_songs = cursor.fetchall()
    return jsonify(common_songs)


@listeners.route('/listeners/seeArtists', methods=['GET'])
def seeArtists():
    cursor = db.get_db().cursor()
    query = '''
    SELECT name FROM artist
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    return jsonify(theData)


