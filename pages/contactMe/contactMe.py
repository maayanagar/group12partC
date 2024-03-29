from flask import Blueprint, render_template, session, redirect, url_for


# subscribe blueprint definition
contactMe = Blueprint('contactMe', __name__, static_folder='static', static_url_path='/contactMe', template_folder='templates')


# Routes
@contactMe.route('/contactMe')
def index():
    return render_template('6_contactMe.html')
