import json
import time
import sys
sys.path.insert(0, './journeytix/model')
sys.path.insert(0, './journeytix/config')
from request import Request

class Bing(object):

    def __init__(self, origin, destination, onwarddate, returndate=None) -> None:
        self.origin = origin
        self.destination = destination
        self.onwarddate = onwarddate
        self.returndate = returndate 
        pass

    def _build_payload(self):

        # import os
        # print(os.listdir())
    
        with open('./journeytix/config/bing_payload.json', 'r') as sample_payload:
            payload = json.loads(sample_payload.read())

        payload["Request"]["flightShopRequest"]["tripLegs"][0]["source"]["code"] = self.origin
        payload["Request"]["flightShopRequest"]["tripLegs"][0]["destination"]["code"] = self.destination
        payload["Request"]["flightShopRequest"]["tripLegs"][0]["departureDate"] = self.onwarddate
        
        return payload

    def _get_resp(self):

        url = f"https://www.bing.com/travel/api/v1/flightSearch/fetchResults"
        payload = self._build_payload()
        # print(payload)
        request = Request()
        resp = request.post_req(url, payload)
        json_resp = json.loads(resp.text)
        
        return json_resp

    def get_flights(self):
        """
        """
        try:
            json_resp = self._get_resp()
        except:
            time.sleep(3)
            json_resp = self._get_resp()

        flights = json_resp['results']['flightResults']['fltResults'][0]['flightSegments']
        all_journeys = []
        for i, item in enumerate(flights):
            if item['airlineInfo']['airlinesLabel'] == 'Multiple Airlines':
                pass
            else:
                journey_detail = {}
                journey_detail["carrier"] = item['flights'][0]['title']
                journey_detail["carrier_logo"] = "https://images.kiwi.com/airlines/64/{}.png".format(item['flights'][0]['code'].split(' ')[0])
                journey_detail["flight_no" ]= item['flights'][0]['code']
                journey_detail["from"] = json_resp['results']['flightResults']['request'][0]['source']['code'].upper()
                journey_detail["to"] = json_resp['results']['flightResults']['request'][0]['destination']['code'].upper()
                layovers = []
                for i,layover in enumerate(item['stop']['stopsSubLabel'].split(',')):
                    layover_data = {
                        "layover": layover
                    }
                    layovers.append(layover_data)
                journey_detail["layovers"] = layovers                

                journey_detail["deptime"] = item['flights'][0]['rawFlightInfo']['departTime']
                journey_detail["arrtime"] = item['flights'][-1]['rawFlightInfo']['arrTime']
                journey_detail["price_lists"] = item['oneWayPriceAndAvailability']['fltPrc']['total']
                all_journeys.append(journey_detail)

        return all_journeys