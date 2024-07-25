from models.__init__ import CURSOR, CONN
import re
from datetime import datetime
class Booking:
    all = {}

    def __init__(
        self, start_date, end_date, total_price, client_id, destination_id, id=None
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.total_price = total_price
        self.client_id = client_id
        self.destination_id = destination_id
        self.id = self 

    def __repr__(self):
        return (
            f"<Booking {self.id}: {self.start_date}-{self.end_date},"
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
        elif client_id < 1:# or not Client.find_by_id(client_id):
            raise ValueError(
                "Client_id must be a positive integer pointing to an existing client"
            )
        self._client_id = client_id

    @property
    def destination_id(self):
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        if not isinstance(destination_id, int):
            raise TypeError("Destination_id must be an integer")
        elif destination_id < 1:# or not Destination.find_by_id(destination_id):
            raise ValueError(
                "Destination_id must be a positive integer pointing to an existing destination"
            )
        self._destination_id = destination_id

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if not isinstance(start_date, str):
            raise TypeError("Start date must be in string format")
        elif not re.match(
            r"([0][1-9]|[1][0-2])\/([0][1-9]|[12][0-9]|[3][01])\/\d{4}", start_date
        ):
            raise ValueError("start_Date must be in the format MM/DD/YYYY")
        self._start_date = start_date
            
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if not isinstance(end_date, str):
            raise TypeError("End date must be in string format")
        elif not re.match(
            r"([0][1-9]|[1][0-2])\/([0][1-9]|[12][0-9]|[3][01])\/\d{4}", end_date
        ):
            raise ValueError("end_Date must be in the format MM/DD/YYYY")
        self._end_date = end_date

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        if not isinstance(total_price, float):
            raise TypeError("Total price must be in float format")
        elif not re.match(r"[0-9]+\.[0-9]{2}", total_price):
            raise ValueError(
                "Total price must be in the format of float with 2 decimal places"
            )
        self._total_price = total_price
            
    #  Association Methods
    def client(self):
        pass
        return Client.find_by_id(self.client_id) if self.client_id else None
    
    def destination(self):
        pass
        return Destination.find_by_id(self.destination_id) if self.destination_id else None
        
    # creating tables should follow the order of clients, destinations, then bookings
    # dropping tables will go in the order opposite of creation
    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                    CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY,
                        start_date TEXT, 
                        end_date TEXT, 
                        total_price FLOAT, 
                        client_id INTEGER, 
                        destination_id INTEGER
                    );
                """
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            return e 
        
    @classmethod   
    def drop_table(cls):
        try:
            CURSOR.execute(
                """
                    DROP TABLE IF EXISTS bookings;
                """
                )
            CONN.commit()
        except Exception as e:
            CONN.rollback()
            return e 
            
    
