from models.__init__ import CURSOR, CONN
import re


class Client:
    all = {}

    def __init__(self, location, category, cost_per_day):
        self.location = location
        self.category = category
        self.cost_per_day = cost_per_day
        self.id = self

    def __repr__(self):
        return f"<Client {self.id}: {self.location}, {self.category}, {self.cost_per_day}"

    @property
    def location(self):
        return self._location 

    @location.setter
    def name(self, location):
        if isinstance(location, str):
            raise TypeError("name must be in string format")
        elif not re.match(r"^[a-zA-Z]", location):
            raise ValueError("Please fill out location")
        self._location = location

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(self, category):
            raise TypeError("category must be in string format")
        elif not ("nature", "history", "food", "excursion"):
            raise ValueError(
                "category must be one of the options of: nature, history, food, or excursion"
            )
        self._category = category

    @property
    def cost_per_day(self):
        return self._cost_per_day

    @cost_per_day.setter
    def cost_per_day(self, cost_per_day):
        if not isinstance(cost_per_day, float):
            raise TypeError("cost_per_day must be in float format")
        elif not re.match(r"[0-9]+\.[0-9]{2}", cost_per_day):
            raise ValueError("cost_per_day must be in the format of float with 2 decimal places")
        self._cost_per_day = cost_per_day

    # Association Methods

    def bookings(self):
        CURSOR.execute(
            """
            SELECT * FROM bookings
            WHERE client_id = ?
        """,
            (self.id,),
        )
        rows = CURSOR.fetchall()
        return [Booking(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    # Utility ORM Methods

    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                    CREATE TABLE IF NOT EXISTS clients (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        location TEXT, 
                        end_date TEXT, 
                        category TEXT
                    );
                """
            )
            CONN.commit()
        except Exception as e:
            return e

    @classmethod
    def drop_table():
        try:
            CURSOR.execute(
                """
                DROP TABLE IF EXISTS clients;
            """
            )
            CONN.commit()
        except Exception as e:
            return e

    @classmethod
    def create(cls, name, location, end_date, category):
        new_client = cls(name, location, end_date, category)
        new_client.save()
        return new_client

    @classmethod
    def new_from_db(cls):
        CURSOR.execute(
            """ 
                SELECT  * FROM clients
                ORDER BY id DESC
                LIMIT 1;
            """
        )
        row= CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0])
    
    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """ 
                SELECT * FROM clients;
            """
        )
        rows= CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[4], row[0]) for row in rows]
    
    @classmethod
    def find_by_name(cls, name): 
        CURSOR.execute(
            """" 
                SELECT * FROM clients
                WHERE id is ?;
            """,
                (name,),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[4], row[0]) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(
            """" 
                SELECT * FROM clients
                WHERE id is ?;
            """,
                (id,),
        )
        row = CURSOR.fetchone()
        return cls(row[1],  row[2], row[3], row[4], row[0]) if row else None
    
    @classmethod
    def find_or_create_by(cls, name, location, end_date, category):
        return cls.find_by_name(name) or cls.create(
            name, location, end_date, category
        )
        
    # Utility ORM Instance Methods
    def save(self):
        CURSOR.execute(
            """ 
                INSERT INTO clients (name, location, end_date, category)
                VALUES (?, ?, ?, ?);
            """,
                (self.name, self.location, self.end_date, self.category),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        return self
    
    def update(self):
        CURSOR.execute(
            """" 
                UPDATE clients
                SET name = ?, location = ?, end_date = ?, category = ?
                WHERE id = ?
            """, 
                (self.name, self.location, self.end_date, self.category, self.id),
        )
        CONN.commit()
        type(self).all[self] = self
        return self
    
    def dele(self):
        CURSOR.execute(
            """ 
                DELETE FROM clients
                WHERE id = ?
            """,
                (self.id,),
        )
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
        return self
    
from models.booking import Booking 