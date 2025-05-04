# kursinis
“Progress is not achieved by luck or accident, but by working on yourself daily.” - Epictetus.

Hotel Management System – Coursework Report by Martynas Siaurys EEf-24

1. Introduction

a. What is your application?
This project is a Hotel Management System implemented in Python. It simulates core hotel operations such as room allocation, guest check-in/check-out, and room service management. The system leverages Object-Oriented Programming (OOP) and adheres to SOLID principles, PEP8 coding standards, and demonstrates design patterns such as Facade, Aggregation, and Composition.

b. How to run the program?
Ensure you have Python 3.10+ installed.

Save the source file as hotel.py.

To run the unit tests: python -m unittest test_hotel.py

c. How to use the program?
The program exposes a high-level interface via the HotelManager class:

Use add_room() to register rooms.

Use check_in_guest() and check_out_guest() for guest operations.

Use provide_room_service() and provide_food() to deliver services to rooms.

2. Body/Analysis

Design Principles and Implementation
This system applies SOLID principles:

Single Responsibility Principle: Each class (e.g., RoomManager, GuestManager, ServiceManager) has one clear responsibility.

Open/Closed Principle: Room and Service types can be extended (StandardRoom, SuiteRoom, RoomService, etc.) without modifying base classes.

Liskov Substitution Principle: Derived room classes (StandardRoom, SuiteRoom) are substitutable for Room.

Interface Segregation Principle: Interfaces like Service are small and specific.

Dependency Inversion Principle: HotelManager depends on abstractions like Room, Service.

3. Composition and Design Patterns

The HotelManager class uses composition to combine the responsibilities of room, guest, and service managers.

A Facade pattern is applied via HotelManager, simplifying interaction with the system.
