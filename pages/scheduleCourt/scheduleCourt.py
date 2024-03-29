from flask import Blueprint, render_template, session, redirect, url_for


# subscribe blueprint definition
scheduleCourt = Blueprint('scheduleCourt', __name__, static_folder='static', static_url_path='/scheduleCourt', template_folder='templates')


# Routes
@scheduleCourt.route('/scheduleCourt')
def index():
    return render_template('5_scheduleCourt.html')