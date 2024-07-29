from models.booking import Booking
from models.destination import Destination
from models.client import Client
from random import sample, choice
from faker import Faker
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
    "food",
    "historic",
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
            Destination.create(
                location = choice(DESTINATIONS), 
                category = choice(category), 
                cost_per_day = fake.random_number(digits=3)
            )
            Client.create(
                name = fake.name(),
                start_date = fake.date_this_year(),
                end_date = fake.date_this_year(),
                category = choice(category),
                destination = choice(DESTINATIONS),
            )
            print("Created destination and client")
        except Exception as e:
            print("Failed to create destination and client due to error: ", e)

    for _ in range(10):
        try:
            destinations = Destination.get_all()
            clients = Client.get_all()
            Booking.create(
                start_date = fake.date_this_year(),
                end_date = fake.date_this_year(),
                total_price = fake.random_number(digits=3),
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
    import ipdb

    ipdb.set_trace()
