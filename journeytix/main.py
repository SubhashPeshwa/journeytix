import sys
sys.path.insert(0, './journeytix/app')
from ticket import Ticket

from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
app = FastAPI()


class JourneyRequest(BaseModel):
    origin: Optional[str] = None
    destination: Optional[str] = None
    onwarddate: Optional[str] = None
    returndate: Optional[str] = None
    source: Optional[str] = None

@app.post("/")
def generate_ticket(journeyrequest: JourneyRequest):
    """
    """
    
    request_json = journeyrequest.dict()
    origin = request_json['origin']
    destination = request_json['destination']
    onwarddate = request_json['onwarddate']
    source = request_json['source']

    ticket = Ticket(origin, destination, onwarddate, source, "")
    resp = ticket.generate_ticket()
    return JSONResponse(content=resp)

@app.get("/")
async def root():
    return {"message": "Keeping things warm in here"}
