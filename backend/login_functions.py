from flask import session, redirect, url_for, request
from backend.db_connection import connect_e_ticket
from werkzeug.security import check_password_hash

# การตรวจสอบการล็อกอิน
def login_required(f):
    def wrap(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('index', error=1))
        return f(*args, **kwargs)
    wrap.__name__ = f.__name__
    return wrap

users = [
    {
        'username': 'admin',
        'password': 'Admin@1'
    }
]
    
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return redirect(url_for('index', error="กรุณากรอกข้อมูลให้ครบถ้วน"))

    for user in users:
        if user['username'] == username and user['password'] == password:
            session['username'] = user['username']
            session.permanent = True

            return redirect(url_for('fda_check_view'))
    else:
        return redirect(url_for('index', error="รหัสผู้ใช้หรือรหัสผ่านไม่ถูกต้อง"))