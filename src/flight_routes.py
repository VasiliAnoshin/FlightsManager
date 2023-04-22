import csv
from datetime import datetime, timedelta
from pydantic import BaseModel
from fastapi import FastAPI
from data_loader import DataLoader
from schemas import Flight
app = FastAPI()

# GET endpoint to get info about a flight
@app.get("/flight-info/{flight_id}")
def get_flight_info(flight_id: str):
    dl = DataLoader()
    return dl.load_flight_info(flight_id)

# POST endpoint to update the CSV file with flights
@app.post("/update-flights")
def update_flights(flights: list[Flight]):
    dl = DataLoader()
    return dl.update_source_file(flights)