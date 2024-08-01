from models.booking import Booking
from models.destination import Destination
from models.client import Client
from random import sample
from faker import Faker

fake = Faker()


def drop_tables():
    Booking.drop_table()
    Destination.drop_table()
    Client.drop_table()


def create_tables():
    Client.create_table()
    Destination.create_table()
    Booking.create_table()


def seed_tables():
    for _ in range(50):
        try:
            Client.create(
                fake.name(),
                fake.date_this_year().strftime("%m/%d/%Y"),
                fake.date_this_year().strftime("%m/%d/%Y"),
                sample(Destination.category_list(), 1)[0],
                sample(Destination.destination_list(), 1)[0],
            )
            Destination.create(
                location=sample(Destination.destination_list(), 1)[0],
                category=sample(Destination.category_list(), 1)[0],
                cost_per_day=fake.pyfloat(
                    right_digits=2, positive=True, max_value=10000
                ),
            )
            print("Created client and destination")
        except Exception as e:
            print("Failed to create client and destination due to error: ", e)

    for _ in range(10):
        try:
            clients = Client.get_all()
            destinations = Destination.get_all()
            Booking.create(
                fake.date_this_year().strftime("%m/%d/%Y"),
                fake.date_this_year().strftime("%m/%d/%Y"),
                fake.pyfloat(right_digits=2, positive=True, max_value=10000),
                sample(clients, 1)[0].id,
                sample(destinations, 1)[0].id,
            )
            print("Created booking")
        except Exception as e:
            print("Failed to create booking due to error: ", e)


if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    seed_tables()
    print("Seed data complete!")
