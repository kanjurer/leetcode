# Parking Lot

Classes:
- ParkingLot
- ParkingSpot
- Vehicle
- Car
- Motorcycle
- Bus


```py
from enum import Enum
from abc import ABC, abstractmethod

class VehicleSize(Enum):
    COMPACT: int = 1
    LARGE: int = 2
    MOTORCYCLE: int = 3


class Vehicle(ABC):
    parking_spot: ParkingSpot
    registration_number: str
    vehicle_size: VehicleSize

    def __init__(self, registration_number: str, vehicle_size: VehicleSize):
        self.registration_number = registration_number
        self.vehicle_size = vehicle_size
        self.parking_spot = None

   def get_vehicle_size(self) -> VehicleSize:
        return self.vehicle_size
    
    def get_registration_number(self) -> str:
        return self.registration_number
    
    def
   
    @abstractmethod