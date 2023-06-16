import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
HEADERS = {
    "apikey": "3wd6k64raWnZh1M8UVVejZjVb1t7LP9U"
}


class FlightSearch:

    def get_destination_code(self, city):
        query = {
            "term": city,
            "locale": "es-ES",
            "location_types": "city",
            "limit": 1
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=query, headers=HEADERS)
        response.raise_for_status()
        iata = response.json()["locations"][0]["code"]
        return iata

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "curr": "MXN"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=HEADERS)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No se encontraron vuelos para {destination_city_code}")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            destination_city=data["cityTo"],
            airlines=data["airlines"]
        )
        print(f"{flight_data.destination_city} : ${flight_data.price}")
        return flight_data