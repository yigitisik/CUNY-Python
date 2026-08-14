import os
from dotenv import load_dotenv
import requests
load_dotenv()

AMADEUS_AUTH_ENDPOINT = f"{os.getenv("AMADEUS_BASE_ENDPOINT")}/v1/security/oauth2/token"
AMADEUS_IATA_ENDPOINT = f"{os.getenv("AMADEUS_BASE_ENDPOINT")}/v1/reference-data/locations/cities"
AMADEUS_FLIGHT_ENDPOINT = f"{os.getenv("AMADEUS_BASE_ENDPOINT")}/v2/shopping/flight-offers"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._apikey = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self.amadeus_params = {
            "grant_type": 'client_credentials',
            "client_id": self._apikey,
            "client_secret": self._api_secret,
        }
        self._token = self._get_new_token()
        self.search_header = {
            "Authorization": f"Bearer {self._token}",
        }

    def _get_new_token(self):
        amadeus_header = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        token_resp = requests.post(url=AMADEUS_AUTH_ENDPOINT, data=self.amadeus_params, headers=amadeus_header)
        return token_resp.json()["access_token"]

    def get_iata_code(self, city):
        keyword_param = {
            "keyword": city
        }
        city_resp = requests.get(url=AMADEUS_IATA_ENDPOINT, params=keyword_param, headers=self.search_header)
        print(f"Status code {city_resp.status_code}. Airport IATA: {city_resp.text}")
        try:
            code = city_resp.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_resp}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_resp}.")
            return "Not Found"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=AMADEUS_FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()

