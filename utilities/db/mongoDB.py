import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

# mongodb connection with one of our users
uri = os.environ.get('DB_URI')

# Create a new client and connect to the server
cluster = MongoClient(uri, server_api=ServerApi('1'))

# database object creation
iTennis_DB = cluster["ITennis"]

# All database's tables
users_col = iTennis_DB['users']
members_col = iTennis_DB['members']
trainingSessions_col = iTennis_DB['sessionsTrainning']


# All database's functions


def add_new_member(member):
    members_col.insert_one(member)


def add_new_user(user):
    users_col.insert_one(user)


def find_user_by_email(email):
    return members_col.find_one({'email': email})


def find_user_by_email_users(email):
    return users_col.find_one({'Email': email})


def get_training_sessions():
    return list(trainingSessions_col.find({}))


def check_and_book_session(session_id):
    # Assume session_id is a string; if it's an ObjectId, convert it accordingly
    session = trainingSessions_col.find_one({'_id': ObjectId(session_id)})
    if session and session.get('status') != 'occupied':
        result = trainingSessions_col.update_one({'_id': ObjectId(session_id)}, {'$set': {'status': 'occupied'}})
        return result.modified_count > 0  # True if the session was successfully updated
    return False  # False if the session is not available or not found
