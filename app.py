from flask import blueprints, render_template, request, redirect, session, jsonify, Flask
#from pymongo.mongo_client import MongoClient
#from pymongo.server_api import ServerApi
from datetime import timedelta, datetime

# mongodb connection with one of our users
#uri = "mongodb+srv://maayann126:MAAYANMAAYAN123456@cluster0.gdvjyvv.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
#cluster = MongoClient(uri, server_api=ServerApi('1'))
#iTennis_DB = cluster["ITennis"]


###### App setup
app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1000)


###### Pages
from pages.homePage.homePage import homePage
app.register_blueprint(homePage)

from pages.clubsDetails.clubsDetails import clubsDetails
app.register_blueprint(clubsDetails)

from pages.loginPage.loginPage import loginPage
app.register_blueprint(loginPage)

from pages.schedule.schedule import schedule
app.register_blueprint(schedule)

from pages.scheduleCourt.scheduleCourt import scheduleCourt
app.register_blueprint(scheduleCourt)

from pages.contactMe.contactMe import contactMe
app.register_blueprint(contactMe)

from pages.history.history import history
app.register_blueprint(history)

from pages.admin.admin import admin
app.register_blueprint(admin)

from pages.subscribe.subscribe import subscribe
app.register_blueprint(subscribe)

from pages.myAccount.myAccount import myAccount
app.register_blueprint(myAccount)

from pages.addSession.addSession import addSession
app.register_blueprint(addSession)

from pages.removeSession.removeSession import removeSession
app.register_blueprint(removeSession)



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