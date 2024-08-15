from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

admins = Blueprint('admins', __name__)

# Monitor all ads (See the list)

# Update status of advertisement
@admins.route('/admins/ad_fetch/<keyword>', methods=['GET'])
def get_songs_on_mood(keyword):
    keyword = request.view_args['keyword']

    # Get a cursor object from the database
    cursor = db.get_db().cursor()

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

# Retrieve list of songs and how much money they earned

# Monitor top 10 artists by revenue or playcount

# Remove a user from the app if needed