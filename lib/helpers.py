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
    print("6. Find an booking by client's id")
    print("7. Find destinations by client's name")
    print("8. Create a new client")
    print("9. Create a new destination")
    print("10. Create a new booking")
    print("11. Update a client")
    print("12. Update a destination")
    print("13. Update an booking")
    print("14. Delete a client")
    print("15. Delete a destination")
    print("16. Delete an booking")
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
            print(destination)
    else:
        print(
            "We are in the process of switching over to a different tourism company and cannot display list of destinations"
        )


def list_bookings():
    if bookings := Booking.get_all():
        for booking in bookings:
            print(booking)
    else:
        print("There are currently no bookings at this time, please try again later")


def find_client_by_name():
    name = input("Enter client's full name: ")
    if len(name.strip()) and re.match(r"^[a-zA-Z]", name) and name.title():
        client = Client.find_by_name(name.title())
        print(client) if client else print("No client found")
    else:
        print("Invalid name")


def find_destination_by_location():
    print("Available Destinations:")
    for index, destination in enumerate(Destination.destination_list(), start=1):
        print(f"{index}. {destination}")
    choice = input("Enter the number corresponding to your destination: ")
    if choice.isdigit() and 1 <= int(choice) <= len(Destination.destination_list()):
        selected_destination = Destination.destination_list()[int(choice) - 1]
        print(f"Destination selected: {selected_destination}")
    else:
        print("Invalid selection. Please enter a valid number.")


def find_booking_by_client_id():
    client_id = input("Enter client's id: ").strip()
    try:
        client_id = int(client_id)
        if client_id > 0:
            booking = Booking.find_by_client_id(client_id)
            if booking:
                print(booking)
            else:
                print("No bookings found")
        else:
            print("Invalid client_id: ID should be a positive integer")
    except ValueError:
        print("Invalid client_id: Please enter a valid number")


def find_destinations_by_client_name():
    name = input("Enter the client's name: ").strip().title()
    try:
        if name and re.match(r"^[a-zA-Z ]+$", name):
            client = Client.find_by_name(name)
            if client:
                print(client.destination)
            else:
                print("No client found with that name")
        else:
            print("Invalid name: Please enter a valid name")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_client():
    name = input("Enter the client's name (i.e. Alicia): ").strip()
    start_date = input("Enter the start date of your trip (MM/DD/YYYY): ").strip()
    end_date = input("Enter the end date of your trip (MM/DD/YYYY): ").strip()
    print("Please select from the list:")
    print(*Destination.category_list())
    print()
    category = input("Enter the category of your interest (from the list): ").strip()
    print()
    print("Please select from the list:")
    print(*Destination.destination_list())
    print()
    destination = input("Enter the destination (from the list): ").strip()

    if (
        len(name)
        and len(start_date)
        and len(end_date)
        and len(category)
        and len(destination)
    ):
        try:
            client = Client.create(
                name.title(), start_date, end_date, category, destination
            )
            print("Successfully created new client!")
            print(client)
        except Exception as e:
            print("Error in creating a new client:", e)
    else:
        print("Invalid input: Ensure all fields are properly filled out!")


def create_destination():
    print()
    print("Please select from the list:")
    print(*Destination.destination_list())
    print()
    location = input("Enter the destination (by city name): ").strip()
    print()
    print("Please select from the list:")
    print(*Destination.category_list())
    print()
    category = input("Enter the category (from the list of options): ").strip()
    cost_per_day = input("Enter the cost per day (e.g. 350.00): ").strip()
    if len(location) and len(category) and len(cost_per_day):
        try:
            destination = Destination.create(
                location.title(), category, float(cost_per_day)
            )
            print(destination)
        except Exception as e:
            print("Error in creating a new destination:", e)
    else:
        print("Invalid location, category, or cost_per_day")


def create_booking():
    start_date = input("Enter the start date of the trip (MM/DD/YYYY): ").strip()
    end_date = input("Enter the end date of the trip (MM/DD/YYYY): ").strip()
    total_price = input("Enter the total price (e.g. 1000.00): ").strip()
    client_id = input("Enter the client's id: ").strip()
    destination_id = input("Enter the destination's id: ").strip()
    if (
        Client.find_by_id(client_id)
        and Destination.find_by_id(destination_id)
        and len(start_date)
        and len(end_date)
        and len(total_price)
        and len(client_id)
        and len(destination_id)
        and re.match(r"^[0-9]+(\.[0-9]{1,2})?$", total_price)
    ):
        try:
            booking = Booking.create(
                start_date,
                end_date,
                float(total_price),
                int(client_id),
                int(destination_id),
            )
            print(booking)
        except Exception as e:
            print("Error creating booking:", e)
    else:
        print("Invalid start date, end date, total price, client id, or destination id")


def update_client_by_id(id, name, start_date, end_date, category):
    try:
        client = Client.find_by_id(id)
        client.name = name.title()
        client.start_date = start_date
        client.end_date = end_date
        client.category = category
        client = client.update()
    except Exception as e:
        raise Exception(e)
    print(client)


def update_client():
    idx = input("Enter the client's id: ").strip()
    name = input("Enter the client's name: ").strip()
    start_date = input("Enter the start date of your trip (MM/DD/YYYY): ").strip()
    end_date = input("Enter the end date of your trip (MM/DD/YYYY): ").strip()
    print()
    print("Please select from the list:")
    print(*Destination.category_list())
    print()
    category = input("Enter the category of your interest (from the list): ").strip()
    if (
        re.match(r"^\d+$", idx)
        and int(idx) > 0
        and len(name)
        and len(start_date)
        and len(end_date)
        and len(category)
    ):
        try:
            update_client_by_id(idx, name, start_date, end_date, category)
        except Exception as e:
            print("Error updating client:", e)
    else:
        print("Invalid id, name, start date, end date, or category")


def update_destination_by_id(id, location, category, cost_per_day):
    try:
        destination = Destination.find_by_id(id)
        destination.location = location.title()
        destination.category = category
        destination.cost_per_day = cost_per_day
        destination = destination.update()
        print(destination)
    except Exception as e:
        raise Exception(e)


def update_destination():
    idx = input("Enter the destination's id: ").strip()
    print()
    print("Please select from the list:")
    print(*Destination.destination_list())
    print()
    location = input("Enter the destination's location: ").strip()
    print()
    print("Please select from the list:")
    print(*Destination.category_list())
    print()
    category = input("Enter the category of your trip: ").strip()
    cost_per_day = input("Enter the cost per day of the trip: ").strip()
    if (
        re.match(r"^\d+$", idx)
        and int(idx) > 0
        and len(location)
        and len(category)
        and len(cost_per_day)
        and re.match(r"^[0-9]+(\.[0-9]{1,2})?$", cost_per_day)
    ):
        try:
            update_destination_by_id(idx, location, category, float(cost_per_day))
        except Exception as e:
            print("Error updating destination:", e)
    else:
        print("Invalid id, location, category, or cost_per_day")


def update_booking_by_id(
    id, start_date, end_date, total_price, client_id, destination_id
):
    try:
        booking = Booking.find_by_id(id)
        booking.start_date = start_date
        booking.end_date = end_date
        booking.total_price = float(total_price)
        booking.client_id = int(client_id)
        booking.destination_id = int(destination_id)
        booking = booking.update()
        print(booking)
    except Exception as e:
        print("Error updating booking:", e)


def update_booking():
    idx = input("Enter the booking's id: ").strip()
    start_date = input("Enter the destination's start date (MM/DD/YYYY): ").strip()
    end_date = input("Enter the destination's end date (MM/DD/YYYY): ").strip()
    total_price = input("Enter the total price of the trip (i.e. 1000.00): ").strip()
    client_id = input("Enter the client's ID: ").strip()
    destination_id = input("Enter the destination's ID: ").strip()
    if (
        re.match(r"^\d+$", idx)
        and int(idx) > 0
        and len(start_date)
        and len(end_date)
        and len(total_price)
        and len(client_id)
        and len(destination_id)
    ):
        try:
            update_booking_by_id(
                idx, start_date, end_date, total_price, client_id, destination_id
            )
        except Exception as e:
            print("Error updating booking:", e)
    else:
        print(
            "Invalid id, start_date, end_date, total_price, client_name, destination_location"
        )


def delete_client_by_id(id):
    try:
        if client := Client.find_by_id(int(id)):
            client.delete()
            print("Client successfully deleted")
        else:
            print("Invalid id")
    except Exception as e:
        raise Exception(e)


def delete_client():
    idx = input("Enter the client's id: ").strip()
    if isinstance(idx, str) and re.match(r"^\d+$", idx) and int(idx) > 0:
        try:
            delete_client_by_id(idx)
        except Exception as e:
            print("Error deleting client:", e)
    else:
        print("Invalid id")


def delete_destination_by_id(id):
    destination = Destination.find_by_id(id)
    destination = destination.delete()
    print("Destination successfully deleted")


def delete_destination():
    idx = input("Enter the destination's id: ")
    if isinstance(idx, str) and re.match(r"^\d+$", idx) and int(idx) > 0:
        try:
            delete_destination_by_id(idx)
        except Exception as e:
            print("Error deleting destination:", e)
    else:
        print("Invalid id")


def delete_booking_by_id(id):
    try:
        booking = Booking.find_by_id(id)
        booking = booking.delete()
        print("Booking successfully deleted")
    except Exception as e:
        raise Exception(e)


def delete_booking():
    idx = input("Enter the booking's id: ")
    if isinstance(idx, str) and re.match(r"^\d+$", idx) and int(idx) > 0:
        try:
            delete_booking_by_id(idx)
        except Exception as e:
            print("Error deleting booking: ", e)
    else:
        print("Invalid id")


def exit_program():
    print("Goodbye!")
    exit()


from models.client import Client
from models.destination import Destination
from models.booking import Booking
