from config import CRUCIBLE_API_KEY, CHALLENGE_URL
import requests
from datetime import datetime
from datetime import timedelta
import numpy as np


class Carbender:
    def __init__(self):
        self.api_key = CRUCIBLE_API_KEY
        self.challenge_url = CHALLENGE_URL
        
    def query(self,input_data):
        response = requests.post(
            f"{CHALLENGE_URL}/submit",
            headers={"X-API-Key": CRUCIBLE_API_KEY},
            json={"bookings": input_data},
        )
        return response
    
    def build_payload(self,car_type,target_date,action,created_date):
        
        payload= {
                "car_type": car_type,
                "date": target_date,
                "action":action,
                "created_date":created_date
            }
        
        return payload
    
    def generate_date_range(self,start_date, end_date):
        """Generate a list of dates between start_date and end_date."""
        date_list = []
        current_date = start_date
        while current_date <= end_date:
            date_list.append(current_date)
            current_date += timedelta(days=7)
        return date_list

    
    def demand_walk(self):

        start_date = datetime(2023, 5, 1)
        end_date = datetime(2023, 5, 28)

        for date in self.generate_date_range(start_date,end_date) :
            print(date)

            target_date = date.strftime("%Y-%m-%d")

            payload = [self.build_payload("sedan",target_date,"book","2023-05-01")]

            response = self.query(payload)

            print(response.json())

    def bender(self):
        end_date = datetime(2023, 5, 22)

        start_date = end_date - timedelta(weeks=6)
        

        all_payload = []

        date_list = self.generate_date_range(start_date,end_date)

        for date in date_list:

            book_payload = self.build_payload("luxury",date.strftime("%Y-%m-%d"),"book","2023-05-01")

            cancel_payload = self.build_payload("luxury",date.strftime("%Y-%m-%d"),"cancel","2023-05-02")

            all_payload.extend([book_payload,cancel_payload])

        response = self.query(all_payload)
        print(response.json())


def main():
    carbender = Carbender()

    carbender.bender()

if __name__ == "__main__":
    main()