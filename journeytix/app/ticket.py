import random
import sys
sys.path.insert(0, './journeytix/model')
from bing import Bing
from keyflight import Keyflight

class Ticket(object):

    def __init__(self, origin, destination, onwarddate, source=None, returndate=None) -> None:
        self.origin = origin
        self.destination = destination
        self.onwarddate = onwarddate
        self.returndate = returndate
        self.source = source
        pass

    def generate_ticket(self):

        if self.source == None:
            source = random.choice(["bing","keyflight"])
        else:
            source = self.source

        if source == "bing":
            try:
                bing = Bing(self.origin, self.destination, self.onwarddate, "")
                ticket_data = bing.get_flights()
            except:
                keyflight = Keyflight(self.origin, self.destination, self.onwarddate, "")
                ticket_data = keyflight.get_flights()    
            return ticket_data
        elif source == "keyflight":
            try:
                keyflight = Keyflight(self.origin, self.destination, self.onwarddate, "")
                ticket_data = keyflight.get_flights()
            except:
                bing = Bing(self.origin, self.destination, self.onwarddate, "")
                ticket_data = bing.get_flights()
            return ticket_data
        else:
            return None
