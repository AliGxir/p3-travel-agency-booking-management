from models.booking import Booking
from models.destination import Destination
from models.client import Client
from random import sample
from faker import Faker
import ipdb
fake = Faker()

DESTINATIONS = [
    "Oahu",
    "Rome",
    "Paris",
    "Tokyo",
    "Amsterdam",
    "Singapore",
    "Bangkok",
    "Hong Kong",
    "New York",
    "San Francisco"
]

category = [
    "nature",
    "historic",
    "food",
    "excursion"
]

def drop_tables():
    Booking.drop_table()
    Client.drop_table()
    Destination.drop_table()


def create_tables():
    Booking.create_table()
    Client.create_table()
    Destination.create_table()


def seed_tables():
    for _ in range(50):
        try:
            # ipdb.set_trace()
            Destination.create(
                location = sample(DESTINATIONS, 1)[0], 
                category = sample(category, 1)[0], 
                cost_per_day = str(fake.pyfloat(right_digits=2, positive=True, max_value=10000))
            )
            Client.create(
                fake.name(),
                fake.date_this_year().strftime("%m/%d/%Y"),
                fake.date_this_year().strftime("%m/%d/%Y"),
                sample(category, 1)[0],
                sample(DESTINATIONS, 1)[0],
            )
            print("Created destination and client")
        except Exception as e:
            print("Failed to create destination and client due to error: ", e)

    for _ in range(10):
        try:
            destinations = Destination.get_all()
            clients = Client.get_all()
            # ipdb.set_trace()
            Booking.create(
                start_date = fake.date_this_year().strftime("%m/%d/%Y"),
                end_date = fake.date_this_year().strftime("%m/%d/%Y"),
                total_price = fake.pyfloat(right_digits=2, positive=True, max_value=10000),
                client_id = sample(clients, 1)[0].id,
                destination_id = sample(destinations, 1)[0].id
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
    # import ipdb

