from flask import Blueprint, render_template, session, redirect, url_for


# subscribe blueprint definition
myAccount = Blueprint('myAccount', __name__, static_folder='static', static_url_path='/myAccount', template_folder='templates')


# Routes
@myAccount.route('/myAccount')
def index():
    return render_template('10_myAccount.html')