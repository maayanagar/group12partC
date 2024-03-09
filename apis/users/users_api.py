# from flask import Blueprint
# from utilities.db.db_manager import dbManager
# from utilities.apis.api_response import json_response
#
# # users_api blueprint definition
# users_api = Blueprint('users_api', __name__)
#
#
# # APIs
# @users_api.route('/users/<int:user_id>')
# @users_api.route('/users/<string:username>')
# @users_api.route('/users')
# def get_users(user_id=None, username=None):
#     if user_id:
#         users_api_data = dbManager.fetch('SELECT * FROM users WHERE id=%s', (user_id,))
#     elif username:
#         users_api_data = dbManager.fetch('SELECT * FROM users WHERE username = %s', (username,))
#     else:
#         users_api_data = dbManager.fetch('SELECT * FROM users')
#     return json_response(users_api_data)
