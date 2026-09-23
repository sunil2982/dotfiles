class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        return False  # Don't suppress exceptions

with MyContext() as ctx:
    print("Inside the context")