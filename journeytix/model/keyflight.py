from bs4 import BeautifulSoup
from requests import get
import json
from lxml import etree
import sys
sys.path.insert(0, './journeytix/model')
from request import Request

class Keyflight(object):

    def __init__(self, origin, destination, onwarddate, returndate=None) -> None:
        self.origin = origin
        self.destination = destination
        self.onwarddate = onwarddate
        self.returndate = returndate 
        pass

    def _build_url(self):
        url = f"https://keyflight.io/tickets/search-ticket?departureAirport={self.origin}&arrivalAirport={self.destination}&departingDateTime={self.onwarddate}"
        return url

    def _get_resp(self):
        """
        """
        request = Request()
        resp = request.get_req(self._build_url())
        soup = BeautifulSoup(resp.text, "html.parser")
        flights = soup.find_all('div', attrs={'class': 'tickets__item'})
        return flights

    def get_flights(self):
        """
        """
        flights = self._get_resp()

        all_journeys = []
        for i,item in enumerate(flights):
            journey_detail = {}
            journey_detail["carrier"] = item.find_all('div', attrs={'class': 'ticket__company-name'})[0].getText().replace('\n','').strip()
            journey_detail["carrier_logo"] = item.find_all('img', attrs={'class': 'ticket__company-img'})[0]['src'].replace('\n','').strip()
            journey_detail["flight_no" ]= item.find_all('div', attrs={'class': 'ticket__flight_no'})[0].getText().replace('\n','').strip()
            journey_detail["from"] = item.find_all('div', attrs={'class': 'ticket__info-label'})[0].find_all('span', attrs={'class': 'ticket__airport'})[0].getText().replace('\n','').strip()
            journey_detail["to"] = item.find_all('div', attrs={'class': 'ticket__info-label'})[1].find_all('span', attrs={'class': 'ticket__airport'})[0].getText().replace('\n','').strip()
            layovers = []
            for i,layover in enumerate(item.find_all('div', attrs={'class': 'ticket__point'})):
                layover_data = {
                    "layover": layover.find_all('span', attrs={'class': 'ticket__airport'})[0].getText().replace('\n','').strip()
                }
                layovers.append(layover_data)
            journey_detail["layovers"] = layovers
            journey_detail["deptime"] = item.find_all('div', attrs={'class': 'ticket__date'})[0].getText().replace('\n','').strip()
            journey_detail["arrtime"] = item.find_all('div', attrs={'class': 'ticket__date'})[1].getText().replace('\n','').strip()
            journey_detail["price_lists"] = item.find_all('div', attrs={'class': 'ticket__price'})[0].getText().replace('\n','').strip()
            all_journeys.append(journey_detail)
        
        return all_journeys