import os
from fastapi import FastAPI
from src.data_loader import DataLoader
from src.schemas import Flight

app = FastAPI()

# GET endpoint to get info about a flight
@app.get("/flight-info/{flight_id}")
def get_flight_info(flight_id: str):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'flights.csv'))
    return DataLoader(file_path).load_flight_info(flight_id)

# POST endpoint to update the CSV file with flights
@app.post("/update-flights")
def update_flights(flights: list[Flight]):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'flights.csv'))
    return DataLoader(file_path).update_source_file(flights)