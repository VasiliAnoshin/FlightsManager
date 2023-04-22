import pandas as pd
import csv
from schemas import Flight

class DataLoader:
    def __init__(self, path_to_file:str) -> None:
        self.file = path_to_file
    
    def load_full_data(self):
        return pd.read_csv(self.file)
    
    def load_flight_info(self, flight_id:int):
        with open('flights.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row['Flight ID'] == flight_id:
                    return row
        
            return {'message': 'Flight not found.'}
    
    def update_source_file(self, flights: list[Flight]):
        if not list:
            raise ValueError('Flights data is empty')
        data = [{'flight ID': flight.flight_id, 'Arrival': flight.arrival, 'Departure': flight.departure, 'success': flight.success} for flight in flights]
        with open('flights.csv', mode='w') as csv_file:
            fieldnames = ['flight ID', 'Arrival', 'Departure', 'success']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            
        return {'message': 'Flights updated successfully.'}
