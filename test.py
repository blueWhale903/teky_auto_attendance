import requests
import datetime
import random
from datetime import date
from datetime import datetime, time

def is_today_weekday():
    today = date.today()
    return today.weekday() < 5

reason = ""
is_weekday = is_today_weekday()

if (is_weekday):
    reason = "Checkin trường ngoài"
else:
    reason = "Checkin cơ sở tân bình"

# API endpoint
url = "https://erp.teky.edu.vn/web/dataset/call_kw/hr.employee/attendance_manual"

# Headers (adjust if needed)
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://erp.teky.edu.vn",
    "Referer": "https://erp.teky.edu.vn/web",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Cookie": "session_id=31995f276b27540d19421d70021e4a6a1ca19bdf; frontend_lang=en_US"
}

# Payload (customize employee ID if needed)
payload_checkin = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "args": [
            [
                8466
            ],
            "hr_attendance.hr_attendance_action_my_attendances",
            "Đi làm việc ở bên ngoài",
            reason
        ],
        "model": "hr.employee",
        "method": "my_attendance_manual",
        "kwargs": {}
    },
    "id": random.randint(100000000, 999999999)
}

payload_checkout = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "args": [
            [
                8466
            ],
            "hr_attendance.hr_attendance_action_my_attendances"
        ],
        "model": "hr.employee",
        "method": "attendance_manual",
        "kwargs": {}
    },
    "id": random.randint(100000000, 999999999)
}

# Send the POST request
# Get the current time
current_time = datetime.now().time()

# Define the target time (5 PM)
five_pm = time(17, 0, 0) # Hour 17 represents 5 PM in 24-hour format

if current_time < five_pm:
    response = requests.post(url, json=payload_checkin, headers=headers)
else:
    response = requests.post(url, json=payload_checkout, headers=headers)

# Output result
if (response.status_code == 200):
    if current_time < five_pm:
        print("✅ Checkin Successfully!")
    else:
        print("✅ Checkout Successfully!")
else:
    print("❌ Checkin/Checkout failed!")

print("Status Code:", response.status_code)
print("Response:", response.text)
