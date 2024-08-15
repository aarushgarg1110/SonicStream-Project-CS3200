from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

admins = Blueprint('admins', __name__)

# Monitor all ads (See the list)
@admins.route('/admins/seeAds', methods=['GET'])
def seeAds():
    cursor = db.get_db().cursor()
    query = '''
    SELECT a.name, a.company, a.target_location, a.target_age, a.status
    FROM advertisement a
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    return jsonify(theData)

# Update status of advertisement
@admins.route('/admins/ad_fetch/<status>/<name>', methods=['PUT'])
def get_songs_on_mood(status, name):

    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    query = '''
            UPDATE advertisement
            SET status = %s
            WHERE LOWER(name) = LOWER(%s)
        '''
    # Execute the query with the keyword parameter

    args = (status, name)
    cursor.execute(query, args)
    db.get_db().commit()

    return f'Updated ad with ID {name} to status {status}'

# top ten artists by likes in the past 30 days
@admins.route('/admins/top_ten_artists', methods=['GET'])
def top_ten_artists():
    cursor = db.get_db().cursor()
    query = '''SELECT a.name, COUNT(ls.liked_on) as likes
            FROM artist a JOIN artist_song asg ON a.id = asg.artist_id
            NATURAL JOIN listener_song ls
            WHERE ls.liked_on >= CURDATE() - interval 30 day
            GROUP BY a.name
            ORDER BY likes DESC
            LIMIT 10;
        '''
    cursor.execute(query)
    theData = cursor.fetchall()
    return jsonify(theData)

# Retrieve list of songs and how much money they earned
@admins.route('/admins/seeMoney', methods=['GET'])
def seeMoney():
    cursor = db.get_db().cursor()
    query = '''
    SELECT s.title, a.name, r.company_revenue
    FROM song s JOIN revenue r ON s.revenue_id = r.id
    JOIN artist_song asg ON asg.song_id = s.id
    JOIN artist a ON a.id = asg.artist_id
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    return jsonify(theData)

# Remove a user from the app if needed
@admins.route('/admins/ban/<username>', methods=['DELETE'])
def ban(username):
    username = request.view_args['username']
    cursor = db.get_db().cursor()
    query = '''
    DELETE FROM listener 
    WHERE username = %s
    '''
    cursor.execute(query, username)
    # theData = cursor.fetchall()
    db.get_db().commit()
    return f'Successfully removed user {username}'