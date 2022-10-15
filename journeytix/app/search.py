import sys
sys.path.insert(0, './journeytix/model')
from airport import Airport

class Search(object):

    def __init__(self, search_term) -> None:
        self.search_term = search_term
        pass

    def search_airport(self):
        airport = Airport(self.search_term)
        airport_search_result = airport.get_airport()
        return airport_search_result