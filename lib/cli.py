from helpers import (
    welcome,
    menu,
    list_clients,
    list_destinations,
    list_bookings,
    find_client_by_name,
    find_destination_by_location,
    find_booking_by_client_id,
    find_destinations_by_client_name,
    create_client,
    create_destination,
    create_booking,
    update_client,
    update_destination,
    update_booking,
    delete_client,
    delete_destination,
    delete_booking,
    exit_program,
)


class CLI:
    def main(self):
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
                find_booking_by_client_id()
            elif choice == "7":
                find_destinations_by_client_name()
            elif choice == "8":
                create_client()
            elif choice == "9":
                create_destination()
            elif choice == "10":
                create_booking()
            elif choice == "11":
                update_client()
            elif choice == "12":
                update_destination()
            elif choice == "13":
                update_booking()
            elif choice == "14":
                delete_client()
            elif choice == "15":
                delete_destination()
            elif choice == "16":
                delete_booking()
            elif choice == "17":
                exit_program()
                break
            else:
                print("Invalid choice")


if __name__ == "__main__":
    cli = CLI()
    cli.main()
