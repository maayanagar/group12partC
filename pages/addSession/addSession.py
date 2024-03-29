from flask import Blueprint, render_template, session, redirect, url_for


# subscribe blueprint definition
addSession = Blueprint('addSession', __name__, static_folder='static', static_url_path='/addSession', template_folder='templates')


# Routes
@addSession.route('/addSession')
def index():
    return render_template('11_addSession.html')