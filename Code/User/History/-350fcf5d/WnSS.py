# TODO: Import the Vehicle class from vehicle.py
from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, vin, make, model, daily_rate, engine_size):
        # TODO: Call the parent class constructor with appropriate parameters
        # TODO: Store engine_size as an instance attribute
        super().__init__(vin,make,model,daily_rate)
        self.engine_size = engine_size
    
    def __str__(self):
        # TODO: Call the parent class's __str__ method to get the base string representation
        # TODO: Return a formatted string that starts with "Motorcycle: " followed by the parent string
        #       and ends with " - {engine_size}cc"
        return f"Motorcycle: {super().__str__()} - {self.engine_size}cc"