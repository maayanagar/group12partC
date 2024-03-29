from flask import Blueprint, render_template, session, redirect, url_for


# subscribe blueprint definition
removeSession = Blueprint('removeSession', __name__, static_folder='static', static_url_path='/removeSession', template_folder='templates')


# Routes
@removeSession.route('/removeSession')
def index():
    return render_template('12_removeSession.html')


