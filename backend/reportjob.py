from flask import request, redirect, url_for, render_template
from flask import redirect, url_for
from backend.db_connection import connect_e_ticket
from mysql.connector import Error
from datetime import datetime

def generate_order_id(conn):
    today_date = datetime.now().strftime('%y%m%d')
    prefix = f"{today_date}#"

    query = f"SELECT * FROM Demo_tb WHERE fda_Num LIKE '{prefix}%' ORDER BY fda_Num DESC LIMIT 1"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        last_order = result[0]
        last_number = int(last_order.split('#')[-1])
        next_number = last_number + 1
    else:
        next_number = 1

    return f"{prefix}{next_number}"

def add_record_sticker(): 
    if request.method == 'POST':
        return redirect(url_for('job'))

    return render_template('reportjob.html')

def dropdown_one():
    agency = [
        "คลังสินค้า-แห้ง",
        "คลังสินค้า-เย็น"
    ]
    return agency

def dropdown_two():
    agency = [
        "สติ๊กเกอร์ - Colorpowder",
        "สติ๊กเกอร์ - Prenature project",
        "สติ๊กเกอร์ - Puree",
        "สติ๊กเกอร์ - Tru-blu",
        "สติ๊กเกอร์ - Tulip Muffin Cup",
        "สติ๊กเกอร์ อื่นๆ",
        "แจ้งปัญหา อื่นๆ"
    ]
    return agency

def dropdown_three():
    quantity = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "10",
        "20"
    ]
    return quantity