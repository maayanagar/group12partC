from flask import Blueprint, render_template, session, request, redirect, url_for
from utilities.db.mongoDB import find_user_by_email_users

loginPage = Blueprint('loginPage', __name__, static_folder='static', static_url_path='/loginPage', template_folder='templates')


@loginPage.route('/loginPage', methods=['GET'])
def loginPage_get():
    return render_template('3_loginPage.html')


@loginPage.route('/loginPage', methods=['POST'])
def loginPage_post():
    email = request.form.get('username')
    password = request.form.get('password')

    user = find_user_by_email_users(email)
    if user:
        if user.get('Password') == password:
            if user.get('Role') == "Customer":
                return render_template('10_myAccount.html', success_message='Welcome to your I-Tennis account')
            else:
                return render_template('8_admin.html', success_message='Welcome to your I-Tennis account')
        else:
            message = 'הסיסמה שגויה'
            return redirect(url_for('loginPage.loginPage_get', message=message))
    else:
        message = 'שם המשתמש לא קיים במערכת'  # Corrected typo
        return redirect(url_for('loginPage.loginPage_get', message=message))
