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
    print("6. Find an booking by start_date or end_date")
    print("7. Create a new client")
    print("8. Create a new destination")
    print("9. Create a new booking")
    print("10. Update a client")
    print("11. Update a destination")
    print("12. Update an booking")
    print("13. Delete a client")
    print("14. Delete a destination")
    print("15. Delete an booking")
    print("16. Find destinations by client's name")
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
    name = input("Enter client's name: ")
    if len(name.strip()) and re.match(r"^[a-zA-Z]", name) and name.title():
        client = Client.find_by_name(name.title())
        print(client) if client else print("No client found")
    else:
        print("Invalid name")
        
def find_destination_by_location():
    location = input("Enter the destination: ")
    if len(location.strip()) and re.match(r"^[a-zA-Z]+(?:\s[a-zA-Z]+)?$", location) and location.title():
        destination = Destination.find_by_location(location.title())
        print(destination) if destination else print("No destination found")
    else:
        print("Invalid destination")
        
def find_booking_by_start_date_or_end_date():
    start_date = input("Enter the start date of the trip (MM/DD/YYYY): ")
    end_date = input("Enter the end date of the trip (MM/DD/YYYY): ")
    if isinstance(start_date, end_date, str) and len(start_date) and len(end_date):
        booking = Booking.find_by_start_or_end_date(start_date, end_date) 
        print(booking) if booking else print("No bookings found")
    else:
        print("Invalid start/end date")
        
def create_client():
    name = input("Enter the client's name: (i.e. Alicia)")
    start_date = input("Enter the start date of your trip (MM/DD/YYYY): ")
    end_date = input("Enter the end date of your trip (MM/DD/YYYY): ")
    category = input("Enter the category of your interest: (from the list)")
    if (
        isinstance(name, str)
        and isinstance(start_date, str)
        and isinstance(end_date, str)
        and isinstance(category, str)
        and len(name)
        and len(start_date)
        and len(end_date)
        and len(category)
    ):
        try:
            client = Client.create(name.title(), start_date, end_date, category.title())
            print(client)
        except Exception as e:
            print("Error in creating a new client: ", e)
    print("Invalid name, start date, end date, or category")
    
def create_destination():
    location = input("Enter the destination: (by city name)") 
    category = input("Enter the category: (from the list of options)")
    cost_per_day = input("Enter the cost per day: (i.e.350.00)")
    if (
        isinstance(location, str)
        and isinstance(category, str)
        and isinstance(cost_per_day, str)
        and len(location)
        and len(category)
        and len(cost_per_day)
    ):
        try:
            destination = Destination.create(location.title(), category, cost_per_day)
            print(destination)
        except Exception as e:
            print("Error in creating a new destination")
    print("Invalid location, category, or cost_per_day")
    
def create_booking():
    start_date = input("Enter the start date of the trip (MM/DD/YYYY): ")
    end_date = input("Enter the end date of the trip (MM/DD/YYYY): ")
    total_price = input("Enter the total price: (i.e. 1000.00)")
    client_id = input("Enter the client's id: ")
    destination_id = input("Enter the destination's id: ")
    if (
        Client.find_by_id(client_id)
        and Destination.find_by_id(destination_id)
        and len(start_date)
        and len(end_date)
        and len(total_price)
        and re.match(r"([0][1-9]|[1][0-2])\/([0][1-9]|[12][0-9]|[3][01])\/\d{4}", start_date)
        and re.match(r"([0][1-9]|[1][0-2])\/([0][1-9]|[12][0-9]|[3][01])\/\d{4}", end_date)
        and re.match(r"[0-9]+\.[0-9]{2}", total_price)
    ):
        try:
            booking = Booking.create(
                start_date, end_date, float(total_price), int(client_id), int(destination_id)
            )
            print(booking)
        except Exception as e:
            print("Error creating booking: ", e)
    print("Invalid start date, end date, total price, client id, or destination id")
    
def exit_program():
    print("Goodbye!")
    exit()
    
def update_client_by_id(id, name, start_date, end_date, category):
    client = Client.find_by_id(id)
    client.name = name.title()
    client.start_date = start_date
    client.end_date = end_date
    client.category = category
    client = client.update()
    print(client)
    
def update_client():
    idx = input("Enter the client's id: ")
    name = input("Enter the client's name: ")
    start_date = input("Enter the start date of your trip (MM/DD/YYYY): ")
    end_date = input("Enter the end date of your trip (MM/DD/YYYY): ")
    category = input("Enter the category of your interest: (from the list)")
    if (
        isinstance(name, str)
        and isinstance(start_date, str)
        and isinstance(end_date, str)
        and isinstance(category, str)
        and re.match(r"^\d+$", idx)
        and int(idx) > 0
        and len(name)
        and len(start_date)
        and len(end_date)
        and len(category)
    ):
        try:
            update_client_by_id(idx, name, start_date, end_date, category)
        except Exception as e:
            print("Error updating client: ", e)
    print("Invalid id, name, start date, end date, or category")
    
def update_destination_by_id(id, location, category, cost_per_day):
    destination = Destination.find_by_id(id)
    destination.location = location.title()
    destination.category = category
    destination.cost_per_day_day = cost_per_day 
    destination = destination.update()
    print(destination)
    
def update_destination():
    idx = input("Enter the destination's id: ")
    location = input("Enter the destination's location: ")
    category = input("Enter the category of your trip: ")
    cost_per_day = input("Enter the cost per day of the trip: ")
    if (
        isinstance(location, str)
        and isinstance(category, str)
        and isinstance(cost_per_day, float)
        and re.match(r"^\d+$", idx)
        and int(idx) > 0
        and len(location)
        and len(category)
        and len(cost_per_day)
    ):
        try:
            update_destination_by_id(idx, location, category, cost_per_day)
        except Exception as e:
            print("Error updating destination: ", e)
    print("Invalid id, location, category, or cost_per_day")
    
def update_booking_by_id(id, start_date, end_date, total_price, client_id, destination_id):
    try:
        booking = Booking.find_by_id(id)
        booking.start_date = start_date
        booking.end_date = end_date
        booking.total_price = float(total_price)
        booking.client_id = client_id
        booking.destination_id = destination_id 
        booking = booking.update()
        print(booking)
    except Exception as e:
        print("Error updating booking: ", e)
        
def updating_booking():
    idx = input("Enter the booking's id: ")
    start_date = input("Enter the destination's start date (MM/DD/YYYY): ")
    end_date = input("Enter the destination's end date (MM/DD/YYYY): ")
    total_price = input("Enter the total price of the trip (i.e. 1000.00): ")
    client_name = input("Enter the client's name: ")
    destination_location = input("Enter the destination's location: ")
    if (
        isinstance(start_date, str)
        and isinstance(end_date, str)
        and isinstance(total_price, float)
        and re.match(r"^\d+$", idx)
        and int(idx) > 0
        and len(start_date)
        and len(end_date)
        and len(total_price)
        and len(client_name)
        and len(destination_location)
    ):
        try:
            update_booking_by_id(idx, start_date, end_date, total_price, client_name, destination_location)
        except Exception as e:
            print("Error updating booking: ", e)
    print("Invalid id, start_date, end_date, total_price, client_name, destination_location")
    
def delete_client_by_id(id):
    if client:= Client.find_by_id(int(id)):
        client.delete()
        print("Client successfully deleted")
    else:
        print("Invalid id")
        
def delete_client():
    idx = input("Enter the client's id: ")
    if isinstance(idx, str) and re.match(r"^\d+$", idx) and int(idx) > 0:
        try: 
            delete_client_by_id(idx)
        except Exception as e:
            print("Error deleting client: ", e)
    print("Invalid id")
    
def delete_destination_by_id(id):
    destination = Destination.find_by_id(id)
    destination = destination.delete()
    print(destination)
    
def delete_destination():
    idx = input("Enter the destination's id: ")
    if isinstance(idx, str) and re.match(r"^\d+$", idx) and int(idx) > 0:
        try:
            delete_destination_by_id(idx)
        except Exception as e:
            print("Error deleting destination: ", e)
    else:
        print("Invalid id")
        
def delete_booking_by_id(id):
    booking = Booking.find_by_id(id)
    booking = booking.delete()
    print(booking)


def delete_booking():
    idx = input("Enter the booking's id: ")
    if isinstance(idx, str) and re.match(r"^\d+$", idx) and int(idx) > 0:
        try:
            delete_booking_by_id(idx)
        except Exception as e:
            print("Error deleting booking: ", e)
    else:
        print("Invalid id")
        
def find_destinations_by_client_name():
    name = input("Enter the client's name ")
    if name and re.match(r"^[a-zA-Z ]+$", name) and name.title():
        if client := Client.find_by_name(name.title()):
            destinations = client.destinations()
            for destination in destinations:
                print(destination())
    else:
        print("Invalid name")
    
    
from models.client import Client
from models.destination import Destination 
from models.booking import Booking