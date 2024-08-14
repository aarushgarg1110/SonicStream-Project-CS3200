from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

admins = Blueprint('admins', __name__)

# Monitor all ads (See the list)

# Update status of advertisement

# Retrieve list of songs and how much money they earned

# Monitor top 10 artists by revenue or playcount

# Remove a user from the app if needed