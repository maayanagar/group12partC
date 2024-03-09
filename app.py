from flask import Blueprint, render_template, request, redirect, session, jsonify, Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import timedelta, datetime

# mongodb connection with one of our users
uri = "mongodb+srv://maayann126:MAAYANMAAYAN123456@cluster0.gdvjyvv.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
cluster = MongoClient(uri, server_api=ServerApi('1'))
iTennis_DB = cluster["ITennis"]


###### App setup
app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1000)


###### Pages
## subscribe
from pages.subscribe.subscribe import subscribe
app.register_blueprint(subscribe)

@app.route('/')
def homePage():
    return render_template('1_homePage.html')


###### Components
## Main menu
# from components.main_menu.main_menu import main_menu
# app.register_blueprint(main_menu)


###### APIs
## Users API
# from apis.users.users_api import users_api
# app.register_blueprint(users_api)

if __name__ == '__main__':
    app.run()