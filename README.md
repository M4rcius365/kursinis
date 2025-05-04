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
------------------------------------------------------------------------------------------------------
2. Body/Analysis

a. Design Principles and Implementation
This system applies SOLID principles:

Single Responsibility Principle: Each class (e.g., RoomManager, GuestManager, ServiceManager) has one clear responsibility.

Open/Closed Principle: Room and Service types can be extended (StandardRoom, SuiteRoom, RoomService, etc.) without modifying base classes.

Liskov Substitution Principle: Derived room classes (StandardRoom, SuiteRoom) are substitutable for Room.

Interface Segregation Principle: Interfaces like Service are small and specific.

Dependency Inversion Principle: HotelManager depends on abstractions like Room, Service.

b. Composition and Design Patterns

The HotelManager class uses composition to combine the responsibilities of room, guest, and service managers.

A Facade pattern is applied via HotelManager, simplifying interaction with the system.
------------------------------------------------------------------------------------------------------
3. Results and Summary

1) The hotel system was successfully implemented using abstraction, encapsulation, inheritance, and polymorphism.
2) SOLID principles are observed; for instance, adding new service types does not require changes to existing code.
3) Thorough test coverage is achieved with unittest and mock, covering all business logic including error handling.
4) Challenges: use of terminals and proper file uploading.
5) Extension possibilities: Integration with a file-based storage system or GUI interface, dynamic pricing, and online booking support.
------------------------------------------------------------------------------------------------------
4. Conclusions

This coursework successfully delivered a modular and testable Hotel Management System using object-oriented programming. The project achieved its goal of modeling real-world hotel operations through well-defined components such as room types, guest management, and service delivery.

The result is a working program that applies SOLID principles, uses abstract classes and design patterns like Facade and Composition, and includes comprehensive unit testing with unittest and mock. The implementation strictly follows PEP8 coding conventions, ensuring code clarity and maintainability.

Looking ahead, the system can be extended by adding features such as persistent data storage, web or GUI interfaces, dynamic pricing, reservation history, and integration with payment systems, making it suitable for real-world use in hospitality applications.
