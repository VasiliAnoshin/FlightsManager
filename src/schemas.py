from pydantic import BaseModel

class Flight(BaseModel):
    flight_id: str
    arrival: str
    departure: str
    success: str
