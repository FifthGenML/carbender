import requests
from datetime import datetime
from src.config import CRUCIBLE_API_KEY, CHALLENGE_URL
import json
from datetime import timedelta
from datetime import datetime

def query(input_data):
    response = requests.post(
        f"{CHALLENGE_URL}/submit",
        headers={"X-API-Key": CRUCIBLE_API_KEY},
        json={"bookings": input_data},
    )
    return response


# Example: Submit a single booking
target_date = datetime(2022, 1, 1)
booking_example = [
    {
        "car_type": "sedan",
        "date": "2023-05-22",
        "action":"book",
        # "created_date": datetime.now().isoformat(),
        "created_date":"2023-05-01"
    },
        {
        "car_type": "sedan",
        "date": "2023-05-22",
        "action":"cancel",
        # "created_date": datetime.now().isoformat(),
        "created_date":"2023-05-02"
    }
]

response = query(booking_example)

print(booking_example)

print(f"\n=== Response Details ===")
print(f"Status Code: {response.status_code}")
print(f"Response Headers: {json.dumps(dict(response.headers), indent=2)}")
print(f"Response Body: {json.dumps(response.json(), indent=2)}")
