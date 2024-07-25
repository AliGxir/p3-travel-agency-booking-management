import sqlite3
# from models.booking import Booking
# from client import Client
# from destination import Destination


CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
