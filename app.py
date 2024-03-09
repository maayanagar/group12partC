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

@app.route('/clubsDetails')
def clubsDetails():
    return render_template('2_clubsDetails.html')

@app.route('/loginPage')
def loginPage():
    return render_template('3_loginPage.html')

@app.route('/schedule')
def schedule():
    return render_template('4_Schedule.html')

@app.route('/scheduleCourt')
def scheduleCourt():
    return render_template('5_scheduleCourt.html')

@app.route('/contactMe')
def contactMe():
    return render_template('6_contactMe.html')

@app.route('/history')
def history():
    return render_template('7_histoy.html')

@app.route('/admin')
def admin():
    return render_template('8_admin.html')

@app.route('/myAccount')
def myAccount():
    return render_template('10_myAccount.html')

@app.route('/addSession')
def addSession():
    return render_template('11_addSession.html')

@app.route('/removeSession')
def removeSession():
    return render_template('12_removeSession.html')

@app.route('/subscribe')
def subscribe():
    return render_template('9_subscribe.html')


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