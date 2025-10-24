# Pizza Price Calculator

```py
# requirements:
"""
- Parking Space Management: Track the availability of parking spaces.
- Vehicle Management: Handle the entry and exit of vehicles.
- Fee Calculation: Calculate parking fees based on parking duration.
- Parking Lot Capacity: Support different types of vehicles with designated spots (e.g., compact, large, handicapped)
"""

# core functionality:
"""
- Parking a Vehicle: Assigning spots to vehicles and recording entry time.
- Unparking a Vehicle: Removing a vehicle and calculating the fee.
- Spot Availability Check: Checking for available spots for specific vehicles.
- Handling Different Vehicle Types: Supporting various vehicle types (e.g., compact, large, electric) with appropriate spot assignments.
"""

# data entity objects:
"""
- ParkingLot
- ParkingSpot
- Vehicle
- ParkingTicket
"""

# functional classes:
"""
- FeeCalculator
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, registration_number, vehicle_type):
        self.registration_number = registration_number
        self.vehicle_type = vehicle_type

class Car(Vehicle):
    # Car specific attributes
    pass

class VehicleType(Enum):
    COMPACT = 1
    LARGE = 2
    HANDICAPPED = 3

    
```
