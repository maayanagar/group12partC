from flask import Blueprint, render_template, session, redirect, url_for


# subscribe blueprint definition
subscribe = Blueprint('subscribe', __name__, static_folder='static', static_url_path='/subscribe', template_folder='templates')


# Routes
@subscribe.route('/subscribe')
def index():
    return render_template('9_subscribe.html')
