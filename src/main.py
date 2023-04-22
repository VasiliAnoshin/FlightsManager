import os
from fastapi import FastAPI, status
from src.data_loader import DataLoader
from src.schemas import Flight

app = FastAPI()

# GET endpoint to get info about a flight
@app.get("/flight-info/{flight_id}", tags=["Flight"], status_code=status.HTTP_200_OK)
def get_flight_info(flight_id: str):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'flights.csv'))
    return DataLoader(file_path).load_flight_info(flight_id)

# POST endpoint to update the CSV file with flights
@app.post("/update-flights", tags=["Flight"], status_code=status.HTTP_200_OK)
def update_flights(flights: list[Flight]):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'flights.csv'))
    return DataLoader(file_path).update_flight_info(flights)