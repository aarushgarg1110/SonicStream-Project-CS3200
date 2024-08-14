from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

artists = Blueprint('artists', __name__)

# Retrieve list of songs and how much money they earned
@artists.route('/artists/revenue/<keyword>', methods=['GET'])
def get_artist_revenue(keyword):
    keyword = request.view_args['keyword']
    cursor = db.get_db().cursor()
    query = '''
        SELECT a.name AS artist_name, s.title as song_title, r.song_payout AS revenue
        FROM artist a
	    JOIN artist_song asg ON a.id = asg.artist_id
	    JOIN song s ON asg.song_id = s.id
	    JOIN revenue r ON s.revenue_id = r.id
        WHERE a.name = %s
        GROUP BY a.name;
    '''
    cursor.execute(query, ('%' + keyword + '%'))
    theData = cursor.fetchall()
    return jsonify(theData)

# Upload a song

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

# Promote a concert
