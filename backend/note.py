from mysql.connector import Error
from backend.db_connection import connect_e_ticket
import random
from datetime import datetime, timedelta
    
def get_fda_tb_sticker():
    try:
        mock_data = []
        names = ["สมชาย", "สมหญิง", "อนันต์", "จันทนา", "ปิยะ", "ศิริพร"]
        departments = ["แผนกบัญชี", "แผนกไอที", "แผนกบุคคล", "แผนกจัดซื้อ", "แผนกคลังสินค้า"]
        subjects = ["เค้กส้ม", "ครีมชีส", "บราวนี่", "กล้วมหอม", "น้ำมัน", "อื่นๆ"]
        statuses = ["Complete", "In Progress", "Cancel"]
        dispatchers = ["admin1", "admin2", "staff1", "staff2"]

        for i in range(20):
            mock_record = {
                "No": i + 1,
                "fda_Num": f"ORD{1000 + i}",
                "Time": (datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M:%S'),
                "REC_Name": random.choice(names),
                "Department": random.choice(departments),
                "Subject": random.choice(subjects),
                "Quantity": random.randint(1, 20),
                "Detail": f"รายละเอียดการขอรายการที่ {i + 1}",
                "status": random.choice(statuses),
                "note": f"หมายเหตุ {i + 1}" if random.random() > 0.3 else "",
                "log": random.choice(dispatchers)
            }
            mock_data.append(mock_record)

        return mock_data
    except Exception as e:
        print(f"Error generating mock sticker data: {e}")
        return []