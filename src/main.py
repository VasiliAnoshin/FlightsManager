import os
from fastapi import FastAPI, status, HTTPException
from src.data_loader import DataLoader
from src.data_writer import DataWriter
from src.schemas import Flight
from src.log import logging
from src.flight_manager import FlightManager
app = FastAPI()
FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'flights.csv'))
logger = logging.getLogger(__name__)

@app.get("/flight-info/{flight_id}", tags=["Flight"], status_code=status.HTTP_200_OK)
def get_flight_info(flight_id: str):
    """
    Get flight information for a specific flight ID.

    Args:
        flight_id (str): The flight ID to retrieve information for.

    Returns:
        dict: A dictionary containing information about the flight, including its
        arrival and departure times, and whether it was a success or a failure.
    """
    try:
        return DataLoader(FILE_PATH).load_flight_info(flight_id)
    except Exception as ex:
        logger.info(f'Unexpected error.  Exception: {ex.args[0]} ')
        raise HTTPException(status_code=500, detail=ex.args[0])

@app.post("/update-flights", tags=["Flight"], status_code=status.HTTP_200_OK)
def update_flights(flights: list[Flight]):
    """
    POST endpoint to update the CSV file with flights.

    Args:
    flights (list[Flight]): A list of Flight objects to be added or updated in the CSV file.

    Returns:
    dict: A dictionary with a 'message' key indicating whether the update was successful or not.
    If the update was successful, the value of the 'message' key will be 'Flights updated successfully'.
    """
    try:
        mng = FlightManager(DataLoader(FILE_PATH).load_full_data())
        df = mng.generarte_success_column()
        writer = DataWriter()
        df = mng.update_flight_info(flights, df)
        writer.save_flight_info(df, FILE_PATH)
        return {'message': 'Flights updated successfully.'}
    except Exception as ex:
        logger.info(f'Unexpected error.  Exception: {ex.args[0]}')
        raise HTTPException(status_code=500, detail=ex.args[0])