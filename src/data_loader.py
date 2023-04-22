import pandas as pd
import csv
from src.schemas import Flight
import numpy as np

class DataLoader:
    def __init__(self, path_to_file:str) -> None:
        self.file = path_to_file
    
    def load_full_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file)
    
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
        with open(self.file, mode='r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['Flight ID'] == flight_id:
                    return row
        
            return {'message': 'Flight not found.'}
    
    def update_source_file(self, flights: list[Flight]) -> dict:
        """Updates a CSV file with the flight information provided.

        Args:
            flights: A list of Flight objects containing the updated flight information.

        Returns:
            A dictionary with a single key-value pair: {'message': 'Flights updated successfully.'}

        Raises:
            ValueError: If the flights data is empty.
        """
        try:
            if not flights:
                raise ValueError('Flights data is empty')
            df = pd.read_csv(self.file)
            for flight in flights:
                if df['Flight ID'].isin([flight.flight_id]).any():
                    raise ValueError(f'flight with the same flight id - {flight.flight_id} already registered.')
                else:
                    df = df.append({'Flight ID': flight.flight_id, 'Arrival': flight.arrival, 'Departure': flight.departure, 'success': np.nan}, 
                              ignore_index= True)
            df.to_csv(self.file, header=False, index=False)
            return {'message': 'Flights updated successfully.'}
        except Exception as ex:
            raise ex
