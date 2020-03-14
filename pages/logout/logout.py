from flask import Blueprint, render_template, session, redirect, url_for


# logout blueprint definition
logout = Blueprint('logout', __name__, static_folder='static', static_url_path='/logout', template_folder='templates')


# Routes
@logout.route('/logout')
def index():
    if 'username' in session:
        session.pop('username') #session.clear()
        return render_template('logout.html')
    else:
        return redirect(url_for('home.index'))