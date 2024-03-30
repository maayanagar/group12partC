from flask import Blueprint, render_template, session, request, redirect, url_for
from utilities.db.mongoDB import find_user_by_email_users

loginPage = Blueprint('loginPage', __name__, static_folder='static', static_url_path='/loginPage',
                      template_folder='templates')


@loginPage.route('/loginPage', methods=['GET'])
def loginPage_get():
    error_message = session.pop('error_message', None)
    return render_template('3_loginPage.html', error_message=error_message)


@loginPage.route('/loginPage', methods=['POST'])
def loginPage_post():
    email = request.form.get('username')  # Modified to match form field name
    password = request.form.get('password')  # Modified to match form field name

    user = find_user_by_email_users(email)
    if user:
        # Compare the stored password hash with the provided password
        if user.get('Password') == password:
            if user.get('Role') == "Customer":
                return render_template('10_myAccount.html', success_message='Welcome to your I-Tennis account')  # Corrected typo
            else:
                return render_template('8_admin.html', success_message='Welcome to your I-Tennis account')  # Corrected typo
        else:
            session['error_message'] = 'Password is incorrect'
            return redirect(url_for('loginPage.loginPage_get'))
    else:
        session['error_message'] = 'Username is incorrect'  # Corrected typo
        return redirect(url_for('loginPage.loginPage_get'))
