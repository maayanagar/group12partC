import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# mongodb connection with one of our users
uri = os.environ.get('DB_URI')

# Create a new client and connect to the server
cluster = MongoClient(uri, server_api=ServerApi('1'))

# database object creation
iTennis_DB = cluster["ITennis"]

# All database's tables
users_col = iTennis_DB['users']
members_col = iTennis_DB['members']


# All database's functions


def add_new_user(user):
    members_col.insert_one(user)

def add_new_user2(user):
    users_col.insert_one(user)

def find_user_by_email(email):
    return members_col.find_one({'email': email})




