from flask import Blueprint, render_template, session, redirect, url_for


# clubsDetails blueprint definition
clubsDetails = Blueprint('clubsDetails', __name__, static_folder='static', static_url_path='/clubsDetails', template_folder='templates')


# Routes
@clubsDetails.route('/clubsDetails')
def index():
    return render_template('2_clubsDetails.html')


