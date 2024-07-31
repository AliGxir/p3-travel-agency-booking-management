#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.client import Client
from models.destination import Destination
from faker import Faker
fake = Faker()

Client.drop_table()
Client.create_table()
client = Client.create("test", "01/01/2024", "02/01/2024", "historic", "New York")
name = fake.name()
ipdb.set_trace()

Destination.drop_table()
Destination.create_table()
destination = Destination("Paris", "nature", fake.pyfloat(right_digits=2, positive=True))
# ipdb.set_trace()