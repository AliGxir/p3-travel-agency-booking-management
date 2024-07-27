# lib/cli.py

from helpers import (
    welcome,
    list_clients,
    list_destinations,
    list_bookings,
    find_client_by_name,
    find_destination_by_location,
    find_booking_by_start_date_or_end_date,
    create_client,
    create_destination,
    create_booking,
    update_client,
    update_destination,
    update_booking,
    delete_client,
    delete_destination,
    delete_booking,
    find_destinations_by_client_name,
    exit_program
)

def main():
    welcome()
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_clients()
        elif choice == "2":
            list_destinations()
        elif choice == "3":
            list_bookings()
        elif choice == "4":
            find_client_by_name()
        elif choice == "5":
            find_destination_by_location()
        elif choice == "6":
            find_booking_by_start_date_or_end_date()
        elif choice == "7":
            create_client()
        elif choice == "8":
            create_destination()
        elif choice == "9":
            create_booking()
        elif choice == "10":
            update_client()
        elif choice == "11":
            update_destination()
        elif choice == "12":
            update_booking()
        elif choice == "13":
            delete_client()
        elif choice == "14":
            delete_destination()
        elif choice == "15":
            delete_booking()
        elif choice == "16":
            find_destinations_by_client_name()
        elif choice == "17":
            exit_program()
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()
