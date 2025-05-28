# SwiftRide
You have been hired by a fictional ride-sharing company, "SwiftRide," to design a software system to manage their ride-sharing operations. The system should:

Allow customers to book rides by providing details: pickup location, drop-off location, and ride types.
Assign drivers to customers based on their availability (available or occupied).
Support three ride types :
Economy : fare = distance *  5
 Luxury : fare = distance * 10
Pool : fare = distance * 3
 4. Provide customers with the estimated ride fare and driver name before confirming the booking.

Your task is to design the system using Object-Oriented Programming (OOP) and SOLID principles and implement it in Python.

Test your software with the following tasks ( Each task is 5 points, total 40 points):

Create fist driver named = “Alice”
Create second driver named = “Bob”
 

Create first customer named = “John”
Create second customer named = “Rebecca”
Create third customer named = “Mike”
 

John wants to go from “Airport” to “Downtown” which is 15 miles using Economy ride.  System should assign the first available driver (Alice) to John and print the fare.  
Output : Ride Fare: $75, Driver: Alice

 

Rebeca wants to go from “College” to “Downtown” which is 10 miles using Luxury ride. System should assign the second available driver (Bob) to Rebeca and print the fare.
Output : Ride Fare: $100, Driver: Bob  

 

Mike wants to go from “Downtown” to “Shopping Mall” which is 5 miles using Pool ride. System should not assign any drivers because none of them are available.
Output : No drivers available.
