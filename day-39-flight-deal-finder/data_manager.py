import os
import requests

from dotenv import load_dotenv
load_dotenv()

SHEET_ENDPOINT=os.getenv("SHEET_ENDPOINT")
sheety_header = {
    "Authorization": f"Bearer {os.getenv('SHEETY_BEARER_TOKEN')}",
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.params = None
        self.row_data = {}

    def get_sheet_request(self):
        get_resp = requests.get(url=SHEET_ENDPOINT, headers=sheety_header)
        get_resp.raise_for_status()

        get_json = get_resp.json()
        print(f"get_json is \n{get_json}\n")
        self.row_data = get_json["prices"]
        return self.row_data

    def put_sheet_request(self):
        for city in self.row_data:
            row_id = city["id"]  # Sheety provides an 'id' for each row
            new_params = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            put_resp = requests.put(
                url=f"{SHEET_ENDPOINT}/{row_id}",
                json=new_params,
                headers=sheety_header
            )
            put_resp.raise_for_status()
            print(f"Updated row {row_id}: {put_resp.text}")
