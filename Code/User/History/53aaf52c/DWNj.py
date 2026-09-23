from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from rental import Rental
from rentalagency import RentalAgency

# Comprehensive test case handler
test_case = input()

if test_case == "create_vehicles":
    # Test vehicle creation
    car = Car("C123", "Toyota", "Camry", 50, 5)
    bike = Motorcycle("M456", "Honda", "CBR", 35, 600)
    
    print(car)
    print(bike)

elif test_case == "rental_workflow":
    # Test rental workflow
    agency = RentalAgency("Quick Rentals")
    
    # Add vehicles
    car = Car("C123", "Toyota", "Camry", 50, 5)
    bike = Motorcycle("M456", "Honda", "CBR", 35, 600)
    agency.add_vehicle(car)
    agency.add_vehicle(bike)
    
    # Check available vehicles
    print(f"Available before rental: {len(agency.available_vehicles())}")
    
    # Rent a vehicle
    rental_id = agency.rent_vehicle("C123", "John Doe", 3)
    print(f"Rental created: {rental_id}")
    
    # Check available vehicles after rental
    print(f"Available after rental: {len(agency.available_vehicles())}")
    
    # Return vehicle
    agency.return_vehicle(rental_id)
    
    # Check available vehicles after return
    print(f"Available after return: {len(agency.available_vehicles())}")

elif test_case == "rental_cost":
    # Test rental cost calculation
    car = Car("C123", "Toyota", "Camry", 50, 5)
    rental = Rental("R1", car, "John Doe", 3)
    print(f"Rental cost for 3 days: ${rental.calculate_cost()}")

elif test_case == "vehicle_methods":
    # Test Vehicle methods
    vehicle = Vehicle("V789", "Generic", "Vehicle", 25)
    print(vehicle)
    print(f"Start rental: {vehicle.start_rental()}")
    print(f"Start rental again: {vehicle.start_rental()}")
    print(f"End rental: {vehicle.end_rental()}")
    print(f"Start rental after end: {vehicle.start_rental()}")

elif test_case == "inheritance_check":
    # Test inheritance relationships
    car = Car("C123", "Toyota", "Camry", 50, 5)
    bike = Motorcycle("M456", "Honda", "CBR", 35, 600)
    
    print(f"Car is a Vehicle: {isinstance(car, Vehicle)}")
    print(f"Motorcycle is a Vehicle: {isinstance(bike, Vehicle)}")
    print(f"Car is a Motorcycle: {isinstance(car, Motorcycle)}")

elif test_case == "polymorphism":
    # Test polymorphic behavior
    vehicles = [
        Vehicle("V789", "Generic", "Vehicle", 25),
        Car("C123", "Toyota", "Camry", 50, 5),
        Motorcycle("M456", "Honda", "CBR", 35, 600)
    ]
    
    for i, v in enumerate(vehicles):
        print(f"Vehicle {i+1}: {v}")

elif test_case == "rental_edge_cases":
    # Test rental edge cases
    agency = RentalAgency("Edge Rentals")
    
    # Try to rent non-existent vehicle
    print(f"Rent non-existent: {agency.rent_vehicle('X999', 'John Doe', 3)}")
    
    # Add a car and rent it
    car = Car("C123", "Toyota", "Camry", 50, 5)
    agency.add_vehicle(car)
    rental_id = agency.rent_vehicle("C123", "John Doe", 3)
    print(f"Valid rental: {rental_id}")
    
    # Try to rent the same car again
    print(f"Rent unavailable car: {agency.rent_vehicle('C123', 'Jane Smith', 2)}")
    
    # Try to return non-existent rental
    print(f"Return non-existent rental: {agency.return_vehicle('R999')}")
    
    # Return the valid rental
    print(f"Return valid rental: {agency.return_vehicle(rental_id)}")
    
    # Try to return the same rental again
    print(f"Return completed rental: {agency.return_vehicle(rental_id)}")

elif test_case == "agency_operations":
    # Test comprehensive agency operations
    agency = RentalAgency("Full Service Rentals")
    
    # Add 5 vehicles
    vehicles = [
        Car("C1", "Toyota", "Camry", 50, 5),
        Car("C2", "Honda", "Accord", 55, 5),
        Car("C3", "Ford", "Focus", 45, 5),
        Motorcycle("M1", "Honda", "CBR", 35, 600),
        Motorcycle("M2", "Yamaha", "R1", 40, 1000)
    ]
    
    for v in vehicles:
        agency.add_vehicle(v)
    
    print(f"Available vehicles: {len(agency.available_vehicles())}")
    
    # Rent 3 vehicles
    rental_ids = [
        agency.rent_vehicle("C1", "Customer 1", 3),
        agency.rent_vehicle("C2", "Customer 2", 5),
        agency.rent_vehicle("M1", "Customer 3", 2)
    ]
    
    print(f"Available after rentals: {len(agency.available_vehicles())}")
    
    # Return 2 vehicles
    agency.return_vehicle(rental_ids[0])
    agency.return_vehicle(rental_ids[1])
    
    print(f"Available after returns: {len(agency.available_vehicles())}")
    
    # Print available vehicles
    print("Available vehicles:")
    for v in agency.available_vehicles():
        print(f"  {v}")

elif test_case == "stress_test":
    # Stress test with many vehicles
    agency = RentalAgency("Stress Test Rentals")
    
    # Add 100 vehicles
    for i in range(100):
        if i % 2 == 0:
            vehicle = Car(f"C{i}", "Make{i}", f"Model{i}", 50, 5)
        else:
            vehicle = Motorcycle(f"M{i}", "Make{i}", f"Model{i}", 35, 600)
        agency.add_vehicle(vehicle)
    
    # Rent 50 vehicles
    rental_ids = []
    for i in range(50):
        vin = f"C{i*2}" if i % 2 == 0 else f"M{i*2-1}"
        rental_id = agency.rent_vehicle(vin, f"Customer{i}", 3)
        rental_ids.append(rental_id)
    
    print(f"Available after 50 rentals: {len(agency.available_vehicles())}")
    
    # Return all rentals
    for rental_id in rental_ids:
        agency.return_vehicle(rental_id)
    
    print(f"Available after all returns: {len(agency.available_vehicles())}")

elif test_case == "invalid_inputs":
    # Test with invalid inputs
    car = Car("C123", "Toyota", "Camry", -50, 5)
    print(f"Car with negative rate: {car}")
    
    bike = Motorcycle("M456", "Honda", "CBR", 35, 0)
    print(f"Motorcycle with zero engine: {bike}")
    
    rental_zero = Rental("R1", car, "John Doe", 0)
    print(f"Rental with zero days cost: ${rental_zero.calculate_cost()}")
    
    rental_neg = Rental("R2", car, "Jane Smith", -3)
    print(f"Rental with negative days cost: ${rental_neg.calculate_cost()}")