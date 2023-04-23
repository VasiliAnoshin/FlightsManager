import pandas as pd
import csv
import numpy as np
from logging import Logger

class DataLoader:
    def __init__(self, path_to_file:str) -> None:
        self.file = path_to_file
    
    def load_full_data(self) -> pd.DataFrame:
        try:
            return pd.read_csv(self.file)
        except Exception as ex:
            Logger.info(f'Unexpected error.  Exception: {ex} ')
    
    def load_flight_info(self, flight_id:int) -> dict:
        """Loads flight information from a CSV file.

        Args:
            flight_id: An integer representing the unique identifier for the flight.

        Returns:
            A dictionary containing information about the flight, including its ID,
            airline, origin, destination, and departure and arrival times. If the
            flight with the specified ID is not found in the file, the function returns
            a dictionary with a single key-value pair: {'message': 'Flight not found.'}
        """
        try:
            with open(self.file, mode='r', encoding='utf-8-sig') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if row['Flight ID'] == flight_id:
                        return row
            
                return {'message': 'Flight not found.'}
        except Exception as ex:
            Logger.info(f'Unexpected error.  Exception: {ex} ')
            return {'message': f'Unexpected error.  For more information check logs.'}
    
    
