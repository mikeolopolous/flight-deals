import requests

SHEETY_ENDPOINT = ""
SHEETY_TOKEN = {"Authorization": ""}


class DataManager:

    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/prices", headers=SHEETY_TOKEN)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/prices/{city['id']}",
                json=new_data,
                headers=SHEETY_TOKEN
            )

            response.raise_for_status()
    

    def update_lowest_price(self):
        print(self.destination_data)
