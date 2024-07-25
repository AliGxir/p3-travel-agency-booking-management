from models.__init__ import CURSOR, CONN
import re
from datetime import datetime

class Booking:
    all = {}
    
    def __init__(self, date, destination, total_price, client_id, destination_id, id=None)
        self.date = date
        self.destination = destination
        self.total_price = total_price
        self.client_id = client_id
        self.destination_id = destination_id
        self.id = id
        
    def __repr__(self):
        return (
            f"<Booking {self.id}: {self.date} {self.destination},"
            + f"{self.total_price},"
            + f"Client ID: {self.client_id},"
            + f"Destination ID: {self.destination_id}>"
        )
    
    # Attributes and Properties    
    @property
    def client_id(self):
        return self._client_id
    
    @client_id.setter
    def client_id(self, client_id):
        if not isinstance(client_id, int):
            raise TypeError("Client_id must be an integer")
        elif client_id < 1 or not Client.find_by_id(client_id):
            raise ValueError("Client_id must be a positive integer pointing to an existing client")
        else: self._client