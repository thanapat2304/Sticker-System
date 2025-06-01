from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import timedelta
from backend.reportjob import add_record_sticker, dropdown_one, dropdown_two, dropdown_three
from backend.reportjob_MS import add_record_sticker_MS, dropdown_one_MS, dropdown_two_MS, dropdown_three_MS
from backend.note import get_fda_tb_sticker
from backend.login_functions import login_required, login
from backend.forcheck import update_status
import requests, calendar
from datetime import datetime
from backend.db_connection import connect_e_ticket
from backend.total import fetch_COUNT_Total , fetch_COUNT_Succeed_Total, fetch_COUNT_Reject_Total, fetch_COUNT_Pending_Total, get_topic_data, fetch_monthly_record_count

app = Flask(__name__)
app.secret_key = '000000000000000000'
app.permanent_session_lifetime = timedelta(minutes=30)

def send_telegram_notify(message, token, chat_id):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.status_code

global_alert_status = False

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    global global_alert_status
    if request.method == 'POST':
        global_alert_status = not global_alert_status
        return redirect(url_for('admin'))
    return render_template('admin.html', alert_status=global_alert_status)

@app.route('/login')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        return login()
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('dashboard'))

@app.route('/job', methods=['GET', 'POST'])
def job():
    current_time = datetime.now().strftime('%d/%m/%Y %H:%M')
    agency = dropdown_one()
    types = dropdown_two()
    quantity = dropdown_three()
    alert_status = session.get('printer_error', False)
    if request.method == 'POST':

        message = f"""
        DateTime : {current_time}
        Name : {request.form['REC_Name']}
        Department : {request.form['REC_Department']}
        Subject : {request.form['REC_Subject']}
        จำนวน : {request.form['REC_Quantity']} แผ่น
        Detail : {request.form['REC_Details']}
        https://portfolio-crg1.onrender.com
        """

        token = '#'
        chat_id = '-#'

        send_telegram_notify(message, token, chat_id)

        return add_record_sticker()

    return render_template('reportjob.html', agency=agency, types=types, quantity=quantity, alert_status=alert_status)

@app.route('/job_MS', methods=['GET', 'POST'])
@login_required
def job_MS():
    current_time = datetime.now().strftime('%d/%m/%Y %H:%M')
    agency = dropdown_one_MS()
    types = dropdown_two_MS()
    quantity = dropdown_three_MS()
    alert_status = session.get('printer_error', False)
    if request.method == 'POST':

        message = f"""
        DateTime : {current_time}
        Name : {request.form['REC_Name']}
        Department : {request.form['REC_Department']}
        Subject : {request.form['REC_Subject']}
        จำนวน : {request.form['REC_Quantity']} แผ่น
        Detail : {request.form['REC_Details']}
        https://portfolio-crg1.onrender.com
        """

        token = '#'
        chat_id = '-#'

        send_telegram_notify(message, token, chat_id)

        return add_record_sticker_MS()

    return render_template('reportjob_MS.html', agency=agency, types=types, quantity=quantity, alert_status=alert_status)

@app.route('/note')
def fda_sticker_view():
    total_data = get_fda_tb_sticker()
    alert_status = session.get('printer_error', False)
    if not total_data:
        return render_template('note.html', results=[])
    return render_template('note.html', results=total_data, alert_status=alert_status)

@app.route('/check')
@login_required
def fda_check_view():
    total_data = get_fda_tb_sticker()
    if not total_data:
        return render_template('forcheck.html', results=[])
    return render_template('forcheck.html', results=total_data)

@app.route('/update_status/<int:id>', methods=['POST'])
def update_status_view(id):
    return update_status(id)

@app.route('/reject_reason/<int:id>', methods=['GET', 'POST'])
def reject_reason_form(id):
    if request.method == 'POST':
        reason = request.form.get('reason')
        conn = connect_e_ticket()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE fda_tb_sticker SET status = %s, note = %s WHERE id = %s", ('Cancel', reason, id))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('fda_check_view'))
        return "Error occurred while updating data."
    return render_template('reject_reason_form.html', id=id)

@app.route('/')
def dashboard():
    current_day = datetime.now().day
    current_month_number = datetime.now().month
    current_month = calendar.month_abbr[current_month_number]
    current_year = datetime.now().year
    total__COUNT_Succeed = fetch_COUNT_Succeed_Total()
    total_COUNT_Reject = fetch_COUNT_Reject_Total()
    total_COUNT_Pending = fetch_COUNT_Pending_Total()
    total_COUNT_Total = fetch_COUNT_Total()
    current_time = datetime.now().strftime("%d %B %Y %H:%M")
    data = get_topic_data()
    topics = [row['Subject'] for row in data]
    counts = [row['topic_count'] for row in data]
    global global_alert_status

    return render_template('total.html', alert_status=global_alert_status, current_time=current_time, total__COUNT_Succeed=total__COUNT_Succeed, total_COUNT_Reject=total_COUNT_Reject, total_COUNT_Pending=total_COUNT_Pending
                           ,total_COUNT_Total=total_COUNT_Total, topics=topics, counts=counts, current_day=current_day, current_month=current_month, current_year=current_year)

@app.route('/monthly-data', methods=['GET'])
def monthly_data():
    data = fetch_monthly_record_count()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True ,host='0.0.0.0', port=8080)