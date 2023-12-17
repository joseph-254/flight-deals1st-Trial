#This class is responsible for structuring the flight data.
import requests
from datetime import datetime , timedelta


FLIGHT_SEARCH_API = "zXya_7z9u4rG4nRooFE9e8-NJm5dCmFC"
# FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2"



class FlightData:
    def __init__(self, price, departure_airport_code, departure_city):
        self.flight_price = price
        self.dpt_airport = departure_airport_code
        self.dpt_city = departure_city


    def flight_data(self ):

        present_date = datetime.now()
        tomorrow_date = present_date + timedelta(1)
        date_to = present_date + timedelta(6*30)

        header = {
            "apikey": FLIGHT_SEARCH_API
        }

        flight_parameters = {
            "fly_from": 'LON',
            "fly_to": "SFO",
            "date_from": tomorrow_date.strftime('%d/%m/%Y'),
            "date_to": date_to.strftime('%d/%m/%Y')
        }

        flight_response = requests.post(url=f"{TEQUILA_ENDPOINT}/search", params=flight_parameters, headers=header)
        print(flight_response.raise_for_status())

flights = FlightData()
flights.flight_data()
