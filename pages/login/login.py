from flask import Blueprint, render_template, request, session
from consts.consts import methods


login = Blueprint('login', __name__, static_folder='static', static_url_path='/login', template_folder='templates')


@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == methods['post']:
        session['username'] = request.form['username']
        return render_template('logged_in.html', username=session.get('username'))
    elif request.method == methods['get']:
        return render_template('login.html')
