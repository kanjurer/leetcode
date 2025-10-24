from typing import Callable
from enum import Enum
from abc import ABC, abstractmethod

class Hotel:
    name: str
    location: str
    
    def __init__(self, name):
        self.name = name
        
        
class HotelFilter:
    @staticmethod
    def by_name(hotel: Hotel, name: str):
        return hotel.name == name

    @staticmethod
    def by_city(hotel: Hotel, city: str):
        return hotel.city == city


class HotelManagementSystem:
    hotels: list[Hotel]
    
    def __init__(self, hotels=[]):
        self.hotels = hotels

    def search(self, func: Callable) -> list[Hotel]:
        return filter(func, self.hotels)


class RoomType(Enum):
    SINGLE = 0
    DOUBLE = 1

    
class Room:
    room_type: RoomType
    room_number: int
    
    def __init__(self, room_type, room_number):
        self.room_type = room_type
        self.room_number = room_number
    





class RoomBooking(ABC):
    @abstractmethod
    def book_room(self, room: Room):
        pass


class OnlineRoomBooking(RoomBooking):
    
    def book_room(self, room):
        return super().book_room(room)

