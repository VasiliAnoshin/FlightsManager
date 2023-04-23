from data_loader import DataLoader
class FlightManager:
    # Define the maximum number of successes allowed per day
    MAX_SUCCESS = 20

    # Define the minimum time difference required for a flight to be considered a success (in minutes)
    MIN_TIME_DIFF = 180
    def __init__(self) -> None:
        self.data_loader = DataLoader()
    
