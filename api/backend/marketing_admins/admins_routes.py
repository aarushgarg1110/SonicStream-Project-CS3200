from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

admins = Blueprint('admins', __name__)

# Monitor all ads (See the list)

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

"""@admins.route('/admins/ad_update/<keyword>', methods=['GET'])
def update_ad(keyword):
    data = request.json

    id = data['id']
    status = data['status']

    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Use parameterized query to avoid SQL injection
    query = '''
        UPDATE advertisement
        SET status = %s
        WHERE id = %s
    '''

    # Execute the query with the keyword parameter
    cursor.execute(query, (status, id))

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    return jsonify(theData)
    """

"""@admins.route('/admins/ad_fetch/<keyword>', methods=['GET'])
def get_songs_on_mood(keyword):
    keyword = request.view_args['keyword']

    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    query = '''
            UPDATE advertisement
            SET status = %s
            WHERE id = %s
        '''
    # Execute the query with the keyword parameter
    cursor.execute(query, (status, id))
    # Use parameterized query to avoid SQL injection
    query = '''
        SELECT * 
        FROM advertisement
        WHERE id = %s
    '''

    # Execute the query with the keyword parameter
    cursor.execute(query, keyword)

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    return jsonify(theData)"""

# Retrieve list of songs and how much money they earned

# Monitor top 10 artists by revenue or playcount

# Remove a user from the app if needed