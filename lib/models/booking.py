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
        elif client_id < 1 or not Client.find_by_id(client_id):
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
        elif destination_id < 1 or not Destination.find_by_id(destination_id):
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
        # elif not re.match(r"[0-9]+\.[0-9]{2}", total_price):
        #     raise ValueError(
        #         "Total price must be in the format of float with 2 decimal places"
            # )
        self._total_price = total_price

    #  Association Methods
    def client(self):
        pass
        return Client.find_by_id(self.client_id) if self.client_id else None

    def destination(self):
        pass
        return (
            Destination.find_by_id(self.destination_id) if self.destination_id else None
        )


    # Helper Methods
    def in_the_future_start_date(self, start_date):
        pass
    
    def in_the_future_end_date(self, end_date):
        pass
        
    # creating tables should follow the order of clients, destinations, then bookings
    # dropping tables will go in the order opposite of creation
    
    # Utility ORM Class Methods
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
        
    @classmethod
    def create(cls, start_date, end_date, total_price, client_id, destination_id):
        new_booking = cls(start_date, end_date, total_price, client_id, destination_id)
        new_booking.save()
        return new_booking
    
    @classmethod
    def new_from_db(cls):
        CURSOR.execute(
            """ 
                SELECT  * FROM bookings
                ORDER BY id DESC
                LIMIT 1;
            """
        )
        row= CURSOR.fetchone()
        booking = cls(row[1], row[2], row[3], row[4], row[5], row[0])
        cls.all[booking.id] = booking
        return booking
    
    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """ 
                SELECT * FROM bookings;
            """
        )
        rows= CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]
    
    @classmethod
    def find_by_start_or_end_date(cls, start_date, end_date): 
        CURSOR.execute(
            """
                SELECT * FROM bookings
                WHERE start_date is ? AND end_date is ?;
            """,
                (start_date, end_date),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[5], row[0]) if row else None
    
    # @classmethod
    # def find_by_total_price(cls, total_price):
    #     CURSOR.execute(
    #         """ 
    #             SELECT * FROM bookings
    #             WHERE total_price is ?;
    #         """,
    #             (total_price,),
    #     )
    #     row = CURSOR.fetchone()
    #     return cls(row[1],  row[2], row[3], row[4], row[5], row[0]) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(
            """
                SELECT * FROM bookings
                WHERE id is ?;
            """,
                (id,),
        )
        row = CURSOR.fetchone()
        return cls(row[1],  row[2], row[3], row[4], row[5], row[0]) if row else None
    
    @classmethod
    def find_or_create_by(cls, start_date, end_date, total_price, client_id, destination_id):
        return cls.find_by_start_or_end_date(start_date, end_date) or cls.create(
            start_date, end_date, total_price, client_id, destination_id
        )
        
    # Utility ORM Instance Methods
    def save(self):
        CURSOR.execute(
            """ 
                INSERT INTO bookings (start_date, end_date, total_price, client_id, destination_id)
                VALUES (?, ?, ?, ?, ?);
            """,
                (self.start_date, self.end_date, self.total_price, self.client_id, self.destination_id),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        return self
    
    def update(self):
        CURSOR.execute(
            """
                UPDATE bookings
                SET start_date = ?, end_date = ?, total_price = ?
                WHERE id = ?
            """, 
                (self.start_date, self.end_date, self.total_price, self.id),
        )
        CONN.commit()
        type(self).all[self] = self
        return self
    
    def delete(self):
        CURSOR.execute(
            """ 
                DELETE FROM bookings
                WHERE id = ?
            """,
                (self.id,),
        )
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
        return self
    
from models.client import Client
from models.destination import Destination
