# SwiftRide
You have been hired by a fictional ride-sharing company, "SwiftRide," to design a software system to manage their ride-sharing operations. The system should:

1. Allow customers to book rides by providing details: pickup location, drop-off location, and ride types.
2. Assign drivers to customers based on their availability (available or occupied).
3. Support three ride types :
*** Economy : fare = distance *  5 ***
- Luxury : fare = distance * 10
- Pool : fare = distance * 3
4. Provide customers with the estimated ride fare and driver name before confirming the booking.

Your task is to design the system using Object-Oriented Programming (OOP) and SOLID principles and implement it in Python.

**Test your software with the following tasks**

1. Create fist driver named = “Alice”
2. Create second driver named = “Bob”
 

3. Create first customer named = “John”
4. Create second customer named = “Rebecca”
5. Create third customer named = “Mike”
 

6. John wants to go from “Airport” to “Downtown” which is 15 miles using Economy ride.  System should assign the first available driver (Alice) to John and print the fare.  
*Output : Ride Fare: $75, Driver: Alice*

 

7. Rebeca wants to go from “College” to “Downtown” which is 10 miles using Luxury ride. System should assign the second available driver (Bob) to Rebeca and print the fare.
*Output : Ride Fare: $100, Driver: Bob*  

 

8. Mike wants to go from “Downtown” to “Shopping Mall” which is 5 miles using Pool ride. System should not assign any drivers because none of them are available.
*Output : No drivers available.*
