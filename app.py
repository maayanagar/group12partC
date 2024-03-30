from flask import Flask
from datetime import timedelta, datetime

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

if __name__ == '__main__':
    app.run()