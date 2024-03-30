from flask import Blueprint, render_template, request, url_for, session, redirect
from utilities.db.mongoDB import *

subscribe = Blueprint('subscribe', __name__, static_folder='static', static_url_path='/subscribe', template_folder='templates')


@subscribe.route('/subscribe', methods=['GET'])
def subscribe_get():
    # Check if there's an error message in the session
    return render_template('9_subscribe.html')


@subscribe.route('/subscribe', methods=['POST'])
def subscribe_post():
    subscribtion_type = request.form.get('subscription-type')
    first_name = request.form.get('firstName')
    phone_number = request.form.get('phone')
    email = request.form.get('email')
    password = request.form.get('password')
    age = request.form.get('age')
    gender = request.form.get('gender')
    credit_card = request.form.get('creditCard')
    id = request.form.get('id')
    expiration_date = request.form.get('exp')
    cvv = request.form.get('cvv')

    if find_user_by_email(email):
        # Instead of using flash, directly set an error message in the session
        message = 'כתובת המייל קיימת במערכת'
        return redirect(url_for('subscribe.subscribe_get', message=message))

    new_user = {
        'subscribtion_type': subscribtion_type,
        'first_name': first_name,
        'phone_number': phone_number,
        'email': email,
        'password': password,
        'age': age,
        'gender': gender,
        'credit_card': credit_card,
        'id': id,
        'expiration_date': expiration_date,
        'cvv': cvv,
    }

    new_user2 = {
        'UserID': id,
        'Name': first_name,
        'Age': age,
        'Phone': phone_number,
        'Email': email,
        'Password': password,  # Make sure to hash passwords in a real application!
        'Role': "Customer",
    }
    add_new_member(new_user)
    add_new_user(new_user2)
    # For a successful registration, directly render the myAccount page templates
    # or set a success message in session to show on the redirected page
    return render_template('10_myAccount.html', success_message='Wellcome to your I-Tennis account')
