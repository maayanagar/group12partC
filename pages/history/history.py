from flask import Blueprint, render_template, session, redirect, url_for


# subscribe blueprint definition
history = Blueprint('history', __name__, static_folder='static', static_url_path='/history', template_folder='templates')


# Routes
@history.route('/history')
def index():
    return render_template('7_histoy.html')
