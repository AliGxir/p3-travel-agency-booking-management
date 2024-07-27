# lib/helpers.py
import re

def welcome():
    print("Welcome to Booking with Travel Agency!")

def menu(): 
    print("Please select an option below:")
    print()
    print("1. List all clients")
    print("2. List all destinations")
    print("3. List all bookings")
    print("4. Find a client by name")
    print("5. Find a destination by location")
    print("6. Find an booking by start_date")
    print("7. Create a new client")
    print("8. Create a new destination")
    print("9. Create a new booking")
    print("10. Update a client")
    print("11. Update a destination")
    print("12. Update an booking")
    print("13. Delete a client")
    print("14. Delete a destination")
    print("15. Delete an booking")
    print("16. Find clients by destination location")
    print("17. Exit")
    
def list_clients():
    if clients := Client.get_all():
        for client in clients:
            print(client)
    else:
        print("Our server is down and cannot retrieve list of clients")
        
def list_destinations():
    if destinations := Destination.get_all():
        for destination in destinations:
            print(destinations)
    else:
        print("We are in the process of switching over to a different tourism company and cannot display list of destinations")
        
def list_bookings():
    if bookings := Booking.get_all():
        for booking in bookings:
            print(booking)
    else:
        print("There are currently no bookings at this time, please try again later")
        
def find_client_by_name():
    
    
def exit_program():
    print("Goodbye!")
    exit()
    
from models.client import Client
from models.destination import Destination 
from models.booking import Booking