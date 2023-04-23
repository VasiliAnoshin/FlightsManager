import pandas as pd

class DataWriter:
    def __init__(self):
        ...
    
    def save_flight_info(self, pd:pd.DataFrame, source_file: str) -> bool:
        pd.to_csv(source_file, index=False)
        return True