import sqlite3
# from models.booking import booking
# from models.client import client
# from models.destination import destination


CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
