import pandas as pd
import numpy as np
import pytest
import sys
from pathlib import Path

sys.path.append(Path(__file__).parents[2].as_posix())
sys.path.append(Path(__file__).parents[3].as_posix())
from src.flight_manager import FlightManager
from src.schemas import Flight

class TestFlightManager:
    
    @pytest.fixture(scope='class')
    def flight_data(self):
        data = {
            'Flight ID': ['AA100', 'BB200', 'CC300', 'DD400'],
            'Arrival': ['12:00', '14:00', '16:00', '18:00'],
            'Departure': ['10:00', '12:00', '14:00', '16:00']
        }
        df = pd.DataFrame(data)
        return df

    @pytest.fixture(scope='class')
    def flight_manager(self, flight_data):
        fm = FlightManager(flight_data)
        return fm
    
    def test_generate_success_column(self, flight_manager):
        df = flight_manager.generarte_success_column()
        assert 'success' in df.columns
        assert df['success'].isin(['Success', 'Fail']).all()

    def test_update_flight_info_success(self, flight_manager):
        flight = Flight(flight_id='EE500', arrival='20:00', departure='18:00')
        df = flight_manager.update_flight_info([flight], flight_manager.flight_data)
        assert 'EE500' in df['Flight ID'].values
        assert df.loc[df['Flight ID'] == 'EE500']['Arrival'].values[0] == '20:00'
        assert df.loc[df['Flight ID'] == 'EE500']['Departure'].values[0] == '18:00'

    def test_update_flight_info_existing_flight(self, flight_manager):
        flight = Flight(flight_id='AA100', arrival='20:00', departure='18:00')
        with pytest.raises(ValueError) as ex:
            df = flight_manager.update_flight_info([flight], flight_manager.flight_data)
        assert 'already registered' in str(ex.value)
    
    def test_update_flight_info_invalid_arrival_time(self, flight_manager):
        flight = Flight(flight_id='EE500', arrival='25:00', departure='18:00')
        with pytest.raises(ValueError) as ex:
            df = flight_manager.update_flight_info([flight], flight_manager.flight_data)
        assert 'Invalid arrival time format' in str(ex.value)
    
    def test_update_flight_info_invalid_departure_time(self, flight_manager):
        flight = Flight(flight_id='EE500', arrival='20:00', departure='30:00')
        with pytest.raises(ValueError) as ex:
            df = flight_manager.update_flight_info([flight], flight_manager.flight_data)
        assert 'Invalid departure time format' in str(ex.value)
        
    def test_update_flight_info_empty_flights(self, flight_manager):
        with pytest.raises(ValueError) as ex:
            df = flight_manager.update_flight_info([], flight_manager.flight_data)
        assert 'Flights data is empty' in str(ex.value)