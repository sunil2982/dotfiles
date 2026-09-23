class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        self.connection = None

with DatabaseConnection("users_db") as conn:
    print(f"Using {conn}")
    print("Performing database operations...")




class SafeContext:
    def __enter__(self):
        print("Setting up resources")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleaning up resources")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return False  # Don't suppress the exception

with SafeContext():
    print("Working with resources")
    # raise ValueError("Something went wrong")  # Uncomment to test