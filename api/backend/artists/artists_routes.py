from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

artists = Blueprint('artists', __name__)

# Retrieve list of songs and how much money they earned
@artists.route('/artists/revenue/<fname>/<lname>', methods=['GET'])
def get_artist_revenue(fname, lname):
    fname = request.view_args['fname']
    lname = request.view_args['lname']
    cursor = db.get_db().cursor()
    query = '''
        SELECT s.title as song_title, r.song_payout AS revenue_in_$
        FROM artist a
	    JOIN artist_song asg ON a.id = asg.artist_id
	    JOIN song s ON asg.song_id = s.id
	    JOIN revenue r ON s.revenue_id = r.id
        WHERE a.name = %s
        ORDER BY revenue_in_$ DESC;
    '''
    cursor.execute(query, (fname + ' ' + lname))
    theData = cursor.fetchall()
    return jsonify(theData)

# Upload a song
@artists.route('/artists/songs/upload/<fname>/<lname>/<album>/<title>/<genre>/<duration>', methods=['POST'])
def upload_song(fname, lname, album, title, genre, duration):
    query_revenue = '''
        INSERT INTO revenue (song_payout, company_revenue)
        VALUES (0, 0)
    '''
    
    query_song = '''
        INSERT INTO song (album, title, genre, duration, revenue_id)
        VALUES (%s, %s, %s, %s, %s)
    '''

    query_artist_id = '''
        SELECT id FROM artist WHERE name = %s
    '''

    query_artist_song = '''
        INSERT INTO artist_song (artist_id, song_id)
        VALUES (%s, %s)
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query_revenue)
    revenue_id = cursor.lastrowid
    cursor.execute(query_song, (album, title, genre, duration, revenue_id))
    song_id = cursor.lastrowid
    cursor.execute(query_artist_id, (fname + ' ' + lname))
    artist_row = cursor.fetchone()
    artist_id = artist_row['id']
    cursor.execute(query_artist_song, (artist_id, song_id))
    db.get_db().commit()

    return 'Success'

# Retrieve an artist’s most popular songs
@artists.route('/artists/popularSongs/<fname>/<lname>', methods=['GET'])
def get_artist_songs(fname, lname):
    fname = request.view_args['fname']
    lname = request.view_args['lname']
    cursor = db.get_db().cursor()
    query = '''
        SELECT s.title AS song_title, SUM(ls.playcount) AS total_playcount
        FROM artist a JOIN artist_song asg ON a.id = asg.artist_id
	    JOIN song s ON asg.song_id = s.id
	    JOIN listener_song ls ON s.id = ls.song_id
        WHERE a.name = %s
        GROUP BY s.title
        ORDER BY total_playcount DESC
    '''
    cursor.execute(query, (fname + ' ' + lname))
    theData = cursor.fetchall()
    return jsonify(theData)

# Look at all reviews on a song
@artists.route('/artists/song/reviews', methods=['GET'])
def get_song_reviews(song):
    song = request.view_args[song]
    cursor = db.get_db().cursor()
    query = '''
        SELECT s.title, r.text
        FROM review r
	    JOIN song s ON r.song_id = s.id
        WHERE a.name = %s
        ORDER BY revenue_in_$ DESC;
    '''
    cursor.execute(query, song)
    theData = cursor.fetchall()
    return jsonify(theData)

# Promote a concert
@artists.route('/artists/concerts/upload/<artist>/<venue>/<date>', methods=['POST'])
def upload_concert(artist, venue, date):
    query_concert = '''
        INSERT INTO concert (venue, event_date)
        VALUES (%s, %s)
    '''

    query_artist_concert = '''
        INSERT INTO artist_concert (artist_id, song_id)
        VALUES (%s, %s)
    '''


    cursor = db.get_db().cursor()
    cursor.execute(query_concert, (venue, date))
    song_id = cursor.lastrowid
    cursor.execute(query_artist_concert, (artist, song_id))
    db.get_db().commit()

    return 'Success'