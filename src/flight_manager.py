import pandas as pd
from src.schemas import Flight
import numpy as np
import datetime
from fastapi import HTTPException
from src.log import logger

class FlightManager:
    # Define the maximum number of successes allowed per day
    MAX_SUCCESS = 20

    # Define the minimum time difference required for a flight to be considered a success (in minutes)
    MIN_TIME_DIFF = 180

    def __init__(self, df:pd.DataFrame) -> None:
        self.flight_data = df
        self.success_count = 0
    
    # Define a function to check if a flight is a success
    def _is_success(self, row) -> str:        
        # Calculate the time difference (in minutes)
        time_diff = (row['Dep'] - row['Arr']).total_seconds() / 60
        
        # Check if the flight meets the success criteria
        if self.success_count < FlightManager.MAX_SUCCESS and time_diff >= FlightManager.MIN_TIME_DIFF:
            self.success_count +=1
            return 'Success'
        else:
            return 'Fail'

    def _is_valid_time_format(self, time_str:str) -> bool:
        try:
            datetime.datetime.strptime(time_str, '%H:%M')
            return True
        except ValueError:
            return False
        
    def _in_valid_range(self, time_str:str)->bool:
        try:
            time = datetime.datetime.strptime(time_str, "%H:%M").time()
            return datetime.time(0, 0) <= time <= datetime.time(23, 59)
        except Exception:
            return False


    def generarte_success_column(self) -> pd.DataFrame:
        """Generates a 'success' column in the DataFrame based on the arrival and departure times.
        The 'Arrival' and 'Departure' columns are converted to datetime objects and sorted by arrival time.
        A new column 'success' is generated using the '_is_success' method.
        The 'Arr' and 'Dep' columns are dropped and the index is reset.
        
        Returns:
        pd.DataFrame: The updated flight data with the 'success' column added.
        """
        try:
            self.flight_data['Arr'] = pd.to_datetime(self.flight_data['Arrival'], format='%H:%M')
            self.flight_data['Dep'] = pd.to_datetime(self.flight_data['Departure'], format='%H:%M')
            # Sort the flights by arrival time
            self.flight_data.sort_values('Arr', inplace = True)
            self.flight_data['success'] = self.flight_data.apply(lambda row: self._is_success(row), axis=1)
            self.flight_data = self.flight_data.drop(['Arr','Dep'], axis=1)
            self.flight_data = self.flight_data.reset_index(drop=True)
            return self.flight_data 
        except Exception as ex:
            logger.info(f'Unexpected error.  Exception: {ex} ')
            raise ex

    def update_flight_info(self, flights: list[Flight], df:pd.DataFrame) -> dict:
        """adding the provided flights to an existing dataframe and returns the updated dataframe.

        Args:
        flights (list[Flight]): A list of Flight objects containing the flight information to be added.
        df (pd.DataFrame): The existing dataframe that needs to be updated with the flight information.

        Returns:
        dict: The updated dataframe containing the newly added flight information.
        """
        if not flights:
            raise ValueError('Flights data is empty')
        for flight in flights:
            if df['Flight ID'].isin([flight.flight_id]).any():
                raise ValueError(f'flight with the same flight id - {flight.flight_id} already registered.')
            elif not self._is_valid_time_format(flight.arrival) and not self._in_valid_range(flight.arrival):  
                raise ValueError('Invalid arrival time format')
            elif not self._is_valid_time_format(flight.departure) and not self._in_valid_range(flight.departure): 
                raise ValueError('Invalid departure time format') 
            else:
                df = df.append({'Flight ID': flight.flight_id, 
                                'Arrival': flight.arrival, 
                                'Departure': flight.departure, 
                                'success': np.nan}, 
                            ignore_index= True)
        return df


if __name__ == '__main__':
    ...