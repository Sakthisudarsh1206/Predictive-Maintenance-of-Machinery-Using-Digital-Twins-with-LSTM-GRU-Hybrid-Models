import pandas as pd
import time
from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import DefaultAzureCredential
from datetime import datetime
from azure.core.exceptions import HttpResponseError

class DigitalTwinInterface:
    def __init__(self):
        self.adt_url = "https://sakthi-ADT-instance.api.wcus.digitaltwins.azure.net"
        self.twin_id = "Twin1"  # Replace with your Twin ID
        self.client = DigitalTwinsClient(self.adt_url, DefaultAzureCredential())
    
    def initialize_twin(self):
        """Initialize the digital twin with default properties."""
        initial_twin = {
            "$dtId": self.twin_id,
            "$metadata": {
                "$model": "dtmi:com:example:WindTurbine;1"  # Ensure model ID matches your DTDL
            },
            "WindSpeed": 0.0,
            "Rotation": 0.0,
            "PowerOutput": 0.0,
            "FrontBearingTemp": 20.0,
            "AmbientTemp": 15.0,
            "MainStatus": 0,
            "FaultMsg": False,
            "Service": False,
            "Fault": 0
        }
        
        try:
            self.client.upsert_digital_twin(self.twin_id, initial_twin)
            print("Digital twin initialized successfully.")
        except HttpResponseError as e:
            print(f"Error initializing twin: {e.message}")
    
    def update_twin(self, properties):
        """Update the digital twin with new simulated properties."""
        patch = [{"op": "replace", "path": f"/{key}", "value": value} for key, value in properties.items()]
        
        try:
            self.client.update_digital_twin(self.twin_id, patch)
            print(f"Twin updated successfully at {datetime.now()}")
        except HttpResponseError as e:
            print(f"Error updating twin: {e.message}")

def validate_data(row):
    """Validate and clean the row data, returning None if invalid data is encountered."""
    try:
        # Parse each field with defaults for missing/NaN values
        return {
            "WindSpeed": float(row.get("WindSpeed", 0.0)),
            "Rotation": float(row.get("Rotation", 0.0)),
            "PowerOutput": float(row.get("PowerOutput", 0.0)),
            "FrontBearingTemp": float(row.get("FrontBearingTemp", 20.0)),
            "AmbientTemp": float(row.get("AmbientTemp", 15.0)),
            "MainStatus": int(row.get("MainStatus", 0)),
            "FaultMsg": bool(row.get("FaultMsg", False)),
            "Service": bool(row.get("Service", False)),
            "Fault": int(row.get("Fault", 0))
        }
    except (ValueError, TypeError) as e:
        print(f"Invalid data encountered in row: {row}. Error: {str(e)}")
        return None

def main():
    # Load data from the CSV file
    csv_file_path = r"D:\CADS\merged_SCADA_data_filtered.csv"
    data = pd.read_csv(csv_file_path)
    
    # Initialize the digital twin interface
    twin_interface = DigitalTwinInterface()
    
    # Initialize the digital twin with default values
    twin_interface.initialize_twin()
    
    print("Starting wind turbine simulation with Digital Twin integration using CSV data...")
    
    try:
        # Iterate over each row in the CSV to simulate real-time data feeding
        for index, row in data.iterrows():
            # Validate and clean the row data
            turbine_state = validate_data(row)
            
            # Only update the twin if data is valid
            if turbine_state is not None:
                twin_interface.update_twin(turbine_state)
                time.sleep(2)  # Wait for 2 seconds to simulate live data streaming
            else:
                print(f"Skipping row {index} due to invalid data.")
            
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    except Exception as e:
        print(f"Simulation stopped due to error: {str(e)}")

if __name__ == "__main__":
    main()
