import requests
import datetime
import time
import random

# # Set your target time (24-hour format)
# target_time = "22:30"

# # Wait until the target time
# while datetime.datetime.now().strftime("%H:%M") != target_time:
#     time.sleep(1)

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
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "args": [
            [8466],  # Your employee ID
            "hr_attendance.hr_attendance_action_my_attendances"
        ],
        "model": "hr.employee",
        "method": "attendance_manual",
        "kwargs": {}
    },
    "id": random.randint(1, 1000000)
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)

# Output result
print("Status Code:", response.status_code)
print("Response:", response.text)
