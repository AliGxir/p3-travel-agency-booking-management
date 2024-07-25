from models.bookings import Booking
from models.destinations import Destination
from models.clients import Client
from random import sample
from faker import Faker
fake = Faker()
import requests

DESTINATIONS = [
    "Oahu"
    "Rome"
    "Paris"
    "Tokyo"
    "Amsterdam"
    "Singapore"
    "Bangkok"
    "Hong Kong"
    "New York"
    "San Francisco"
]

def drop_tables():
    pass

def create_table():
    pass

def seed_tables():
    for _ in range(50):
        try:
            destinations = Destination.get_all()
            clients = Client.get_all()
            Booking.create(
                fake.date(),
                fake.destination(),
                fake.total_price(),
                sample(clients, 1)[0].id,
                sample(destinations, 1)[0].id
            )
            print("Created booking")
        except Exception as e:
            print("Failed to create booking due to error: ", e)
            
if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_table()
    print("Tables created!")
    seed_tables()
    print("Seed data complete!")
    import ipdb; ipdb.set_trace()