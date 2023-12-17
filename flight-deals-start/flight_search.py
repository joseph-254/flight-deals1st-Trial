import requests
import datetime as dt
from datetime import timedelta

FLIGHT_SEARCH_API = "zXya_7z9u4rG4nRooFE9e8-NJm5dCmFC"
# FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"



#This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def get_destination_code(self, city_name):
        # code = "TESTING"
        # return code
        location_header = {
            "apikey": FLIGHT_SEARCH_API
        }
        location_parameter = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=location_parameter, headers=location_header)
        # print(response.status_code)
        location_response = response.json()
        results = location_response["locations"]
        code = results[0]["code"]

        return code

# flightlocations = FlightSearch()
# flightlocations.get_destination_code(city)



