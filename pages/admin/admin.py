from flask import Blueprint, render_template, session, redirect, url_for


# subscribe blueprint definition
admin = Blueprint('admin', __name__, static_folder='static', static_url_path='/admin', template_folder='templates')


# Routes
@admin.route('/admin')
def index():
    return render_template('8_admin.html')
