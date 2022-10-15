import sys
import json
sys.path.insert(0, './journeytix/model')
from request import Request

class Airport(object):

    def __init__(self, search_term) -> None:
        self.search_term = search_term
        pass

    def build_url(self):
        url = f"https://api.skypicker.com/locations?limit=20&term={self.search_term}&locale=en-US&X-Client=frontend&location_types=city&location_types=airport&location_types=country"
        return url

    def get_airport(self):
        request = Request()
        resp = request.get_req(self.build_url())
        json_resp = json.loads(resp.text)
        airports = json_resp['locations']
        all_airports = []
        for airport in airports:
            if "country" in airport:
                airport_detail = {}
                airport_detail["code"] = airport["code"]
                airport_detail["name"] = airport["name"]
                all_airports.append(airport_detail)

        return all_airports
