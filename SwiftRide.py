from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional

# SOLID Principles Implementation:
# S - Single Responsibility Principle: Each class has one responsibility
# O - Open/Closed Principle: System is open for extension (new ride types) but closed for modification
# L - Liskov Substitution Principle: RideType implementations can be substituted
# I - Interface Segregation Principle: Interfaces are specific to their purpose
# D - Dependency Inversion Principle: High-level modules depend on abstractions

class DriverStatus(Enum):
    """Enum for driver availability status - SRP: Single responsibility for status constants"""
    AVAILABLE = "available"
    OCCUPIED = "occupied"

class RideType(ABC):
    """Abstract base class for ride types - OCP: Open for extension with new ride types"""
    
    @abstractmethod
    def calculate_fare(self, distance: float) -> float:
        """Calculate fare based on distance"""
        pass
    
    @abstractmethod
    def get_type_name(self) -> str:
        """Get the name of the ride type"""
        pass

class EconomyRide(RideType):
    """Economy ride implementation - SRP: Handles only economy ride logic"""
    
    def calculate_fare(self, distance: float) -> float:
        return distance * 5
    
    def get_type_name(self) -> str:
        return "Economy"

class LuxuryRide(RideType):
    """Luxury ride implementation - SRP: Handles only luxury ride logic"""
    
    def calculate_fare(self, distance: float) -> float:
        return distance * 10
    
    def get_type_name(self) -> str:
        return "Luxury"

class PoolRide(RideType):
    """Pool ride implementation - SRP: Handles only pool ride logic"""
    
    def calculate_fare(self, distance: float) -> float:
        return distance * 3
    
    def get_type_name(self) -> str:
        return "Pool"

class RideTypeFactory:
    """Factory class to create ride types - SRP: Responsible only for creating ride types"""
    
    @staticmethod
    def create_ride_type(ride_type: str) -> RideType:
        """Create ride type based on string input"""
        ride_types = {
            "economy": EconomyRide(),
            "luxury": LuxuryRide(),
            "pool": PoolRide()
        }
        
        ride_type_lower = ride_type.lower()
        if ride_type_lower not in ride_types:
            raise ValueError(f"Invalid ride type: {ride_type}")
        
        return ride_types[ride_type_lower]

class Driver:
    """Driver class - SRP: Manages driver information and status"""
    
    def __init__(self, name: str):
        self.name = name
        self.status = DriverStatus.AVAILABLE
        self.current_ride = None
    
    def is_available(self) -> bool:
        """Check if driver is available"""
        return self.status == DriverStatus.AVAILABLE
    
    def assign_ride(self, ride) -> None:
        """Assign a ride to the driver"""
        if not self.is_available():
            raise ValueError(f"Driver {self.name} is not available")
        
        self.status = DriverStatus.OCCUPIED
        self.current_ride = ride
    
    def complete_ride(self) -> None:
        """Mark ride as complete and make driver available"""
        self.status = DriverStatus.AVAILABLE
        self.current_ride = None

class Customer:
    """Customer class - SRP: Manages customer information"""
    
    def __init__(self, name: str):
        self.name = name
        self.ride_history = []

class Ride:
    """Ride class - SRP: Manages ride information"""
    
    def __init__(self, customer: Customer, pickup_location: str, 
                 dropoff_location: str, distance: float, ride_type: RideType):
        self.customer = customer
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.distance = distance
        self.ride_type = ride_type
        self.fare = ride_type.calculate_fare(distance)
        self.driver = None
        self.is_confirmed = False
    
    def assign_driver(self, driver: Driver) -> None:
        """Assign a driver to this ride"""
        self.driver = driver
        driver.assign_ride(self)
        self.is_confirmed = True

class DriverManager:
    """Manages driver operations - SRP: Responsible only for driver management"""
    
    def __init__(self):
        self.drivers: List[Driver] = []
    
    def add_driver(self, driver: Driver) -> None:
        """Add a new driver to the system"""
        self.drivers.append(driver)
    
    def get_available_driver(self) -> Optional[Driver]:
        """Get the first available driver"""
        for driver in self.drivers:
            if driver.is_available():
                return driver
        return None
    
    def get_all_drivers(self) -> List[Driver]:
        """Get all drivers"""
        return self.drivers.copy()

class RideBookingService:
    """Service for booking rides - SRP: Handles ride booking logic"""
    
    def __init__(self, driver_manager: DriverManager):
        # DIP: Depends on abstraction (DriverManager) not concrete implementation
        self.driver_manager = driver_manager
    
    def book_ride(self, customer: Customer, pickup_location: str, 
                  dropoff_location: str, distance: float, ride_type_str: str) -> Optional[Ride]:
        """Book a ride for a customer"""
        try:
            # Create ride type using factory
            ride_type = RideTypeFactory.create_ride_type(ride_type_str)
            
            # Create ride object
            ride = Ride(customer, pickup_location, dropoff_location, distance, ride_type)
            
            # Try to assign a driver
            available_driver = self.driver_manager.get_available_driver()
            
            if available_driver:
                ride.assign_driver(available_driver)
                customer.ride_history.append(ride)
                return ride
            else:
                return None
                
        except ValueError as e:
            print(f"Error booking ride: {e}")
            return None

class SwiftRideSystem:
    """Main system class - SRP: Coordinates all system operations"""
    
    def __init__(self):
        self.driver_manager = DriverManager()
        self.booking_service = RideBookingService(self.driver_manager)
        self.customers: List[Customer] = []
    
    def add_driver(self, name: str) -> Driver:
        """Add a new driver to the system"""
        driver = Driver(name)
        self.driver_manager.add_driver(driver)
        return driver
    
    def add_customer(self, name: str) -> Customer:
        """Add a new customer to the system"""
        customer = Customer(name)
        self.customers.append(customer)
        return customer
    
    def book_ride(self, customer: Customer, pickup_location: str, 
                  dropoff_location: str, distance: float, ride_type: str) -> None:
        """Book a ride and display result"""
        ride = self.booking_service.book_ride(
            customer, pickup_location, dropoff_location, distance, ride_type
        )
        
        if ride:
            print(f"Ride Fare: ${ride.fare:.0f}, Driver: {ride.driver.name}")
        else:
            print("No drivers available.")

def main():
    """Test the SwiftRide system with the given requirements"""
    # Initialize the system
    system = SwiftRideSystem()
    
    # Task 1 & 2: Create drivers
    alice = system.add_driver("Alice")
    bob = system.add_driver("Bob")
    
    # Task 3, 4, 5: Create customers  
    john = system.add_customer("John")
    rebecca = system.add_customer("Rebecca")
    mike = system.add_customer("Mike")
    
    print("=== SwiftRide System Test ===\n")
    
    # Task 6: John's ride (Airport to Downtown, 15 miles, Economy)
    print("Task 6:")
    system.book_ride(john, "Airport", "Downtown", 15, "Economy")
    
    # Task 7: Rebecca's ride (College to Downtown, 10 miles, Luxury)
    print("\nTask 7:")
    system.book_ride(rebecca, "College", "Downtown", 10, "Luxury")
    
    # Task 8: Mike's ride (Downtown to Shopping Mall, 5 miles, Pool)
    print("\nTask 8:")
    system.book_ride(mike, "Downtown", "Shopping Mall", 5, "Pool")

if __name__ == "__main__":
    main()