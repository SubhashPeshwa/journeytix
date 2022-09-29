import sys
sys.path.insert(0, './app')

from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
app = FastAPI()


class DFRequest(BaseModel):
    responseId: Optional[str] = None
    queryResult: Optional[dict] = None
    originalDetectIntentRequest: Optional[dict] = None
    session: Optional[str] = None

@app.post("/")
def connect_with_db(dfrequest: DFRequest):
    """
    """
    
    request_json = dfrequest.dict()
    query_text = request_json['queryResult'].get('queryText')
    action = request_json.get('queryResult').get('action')

@app.get("/")
async def root():
    return {"message": "Keeping things warm in here"}
