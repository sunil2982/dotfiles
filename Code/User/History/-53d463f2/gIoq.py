class Vehicle:
    def __init__(self, vin, make, model, daily_rate):
        # Initialize properties
        self.vin = vin
        self.make = make
        self.model = model
        self.daily_rate = daily_rate
        self.available = True
    
    def start_rental(self):
        # TODO: Check if the vehicle is available
        # TODO: If available, set self.available to False and return True
        # TODO: If not available, return False
        if self.available:
            self.available =False
            return True
        return False
    def end_rental(self):
        # TODO: Set self.available to True
        # TODO: Return True to indicate successful completion
        self.available = True
        return True
    
    def __str__(self):
        # TODO: Create a status string based on self.available ("Available" or "Not Available")
        # TODO: Return a formatted string in the format: "{make} {model} (VIN: {vin}) - {status}"
        if self.available:
            return  f"{self.make} {self.model} (VIN: {self.vin}) - Available"
        else:
            return f"{self.make} {self.model} (VIN: {self.vin}) - Not Available"