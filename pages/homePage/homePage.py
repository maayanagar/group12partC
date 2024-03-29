from flask import Blueprint, render_template, session, redirect, url_for


# homePage blueprint definition
homePage = Blueprint('homePage', __name__, static_folder='static', static_url_path='/homePage', template_folder='templates')


# Routes
@homePage.route('/')
def index():
    return render_template('1_homePage.html')
