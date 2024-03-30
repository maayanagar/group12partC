from flask import Blueprint, render_template, redirect, url_for, request
from utilities.db.mongoDB import *

schedule = Blueprint('schedule', __name__, static_folder='static', static_url_path='/schedule', template_folder='templates')


@schedule.route('/schedule', methods=['GET'])
def index():
    sessions_data = get_training_sessions()
    schedule_by_day = {}
    # group sessions by day
    for session in sessions_data:
        day = session.get('day')
        if day not in schedule_by_day:
            schedule_by_day[day] = []
        schedule_by_day[day].append(session)
    # sort sessions within each day by time
    for day_sessions in schedule_by_day.values():
        day_sessions.sort(key=lambda s: s['time'])
    days_of_week = ["שבת", "שישי", "חמישי", "רביעי", "שלישי", "שני", "ראשון"]
    sorted_days = sorted(schedule_by_day.keys(), key=lambda d: days_of_week.index(d))
    return render_template('4_Schedule.html', sorted_days=sorted_days, schedule_by_day=schedule_by_day)


@schedule.route('/book-session', methods=['POST'])
def book_session():
    session_id = request.form['sessionId']
    if check_and_book_session(session_id):
        message = 'ההרשמה בוצעה בהצלחה!'
    else:
        message = 'האימון תפוס, אנא בחר אימון אחר.'
    return redirect(url_for('schedule.index', message=message))


