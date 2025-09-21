import requests
import html

OPENTDB_URL = "https://opentdb.com/api.php"
parameters = {
    "amount": 5,
    "category": 18,
    "type": "boolean",
}
opentdb_response = requests.get(url=OPENTDB_URL, params=parameters)
opentdb_response.raise_for_status()
question_data = opentdb_response.json()["results"]
