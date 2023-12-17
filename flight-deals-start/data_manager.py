import requests
from pprint import pprint

# SHEETY_ENDPOINT = "https://api.sheety.co/3aa8bd12d2f7454767bd60b9b5438b45/myFlightDeals/prices/2"
SHEETY_ENDPOINT = "https://api.sheety.co/3aa8bd12d2f7454767bd60b9b5438b45/myFlightDeals/prices"
#This class is responsible for talking to the Google Sheet.

class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.sheet_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        pprint(self.sheet_data, indent=5)
        return self.sheet_data

    def update_destination_data(self):
        for city in self.sheet_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)





    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).

        #----my way ----#
    # def get_destination_data(self):
    #     for data in self.destination_data:
    #         sheety_parameters = {
    #             "City": "",
    #             "IATA Code": "",
    #             "Lowest Price": ""
    #         }
    #         requests.get(url=SHEETY_ENDPOINT, params=sheety_parameters)
    #         print(data.text)