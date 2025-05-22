from backend.db_connection import connect_e_ticket
import random
from datetime import datetime

def fetch_COUNT_Succeed_Total():
    try:
        total_Succeed = random.randint(100, 1000)
        formatted_Succeed = f"{total_Succeed:,}"
        return formatted_Succeed
    except Exception as e:
        print(f"Error generating mock data: {e}")
        return None

def fetch_COUNT_Reject_Total():
    try:
        total_Reject = random.randint(10, 90)
        formatted_Reject = f"{total_Reject:,}"
        return formatted_Reject
    except Exception as e:
        print(f"Error generating mock data: {e}")
        return None
    
def fetch_COUNT_Pending_Total():
    try:
        total_Pending = random.randint(100, 1000)
        formatted_Pending = f"{total_Pending:,}"
        return formatted_Pending
    except Exception as e:
        print(f"Error generating mock data: {e}")
        return None

def fetch_COUNT_Total():
    try:
        total_Total = random.randint(1001, 1400)
        formatted_Total = f"{total_Total:,}"
        return formatted_Total
    except Exception as e:
        print(f"Error generating mock data: {e}")
        return None

def get_topic_data():
    mock_subjects = [
        "เค้กส้ม", 
        "ครีมชีส", 
        "บราวนี่", 
        "กล้วมหอม", 
        "น้ำมัน",
        "อื่นๆ"
    ]

    result = []
    for subject in mock_subjects:
        topic_count = random.randint(10, 200)
        result.append({
            "Subject": subject,
            "topic_count": topic_count
        })

    result.sort(key=lambda x: x["topic_count"], reverse=True)

    return result

def fetch_monthly_record_count():
    try:
        current_year = datetime.now().year
        result = []

        for month in range(1, 13):
            month_year = f"{current_year}-{month:02d}"

            record_count = random.randint(50, 300)

            result.append({
                "month_year": month_year,
                "record_count": record_count
            })

        result.sort(key=lambda x: x["month_year"])
        return result
    except Exception as e:
        print(f"Error generating mock monthly record count: {e}")
        return []