from models.__init__ import CURSOR, CONN
import re
from datetime import datetime

class Booking:
    all = {}
    
    def __init__(self, date, destination, total_price, client_id, destination_id, id=None):
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
        else: self._client_id = client_id
        
    @property
    def destination_id(self):
        return self._destination_id
    
    @destination_id.setter
    def destination_id(self, destination_id):
        if not isinstance(destination_id, int):
            raise TypeError("Destination_id must be an integer")
        elif destination_id < 1 or not Destination.find_by_id(destination_id):
            raise ValueError("Destination_id must be a positive integer pointing to an existing destination")
        else: self._destination_id = destination_id
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise TypeError("Date must be in string format")
        elif not re.match(
            r"([0][1-9]|[1][0-2])\/([0][1-9]|[12][0-9]|[3][01])\/\d{4}", date
        ):
            raise ValueError("Date must be in the format MM/DD/YYYY")
        else:
            self._date = date
    
    @property
    def destination(self):
        pass
    
    @destination.setter
    def destination(self, destination):
        pass
    
    @property
    def total_price(self):
        pass
    
    @total_price.setter
    def total_price(self, total_price):
        pass