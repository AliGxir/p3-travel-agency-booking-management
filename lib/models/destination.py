from models.__init__ import CURSOR, CONN
import re

class Destination:
    all = {}

    def __init__(self, location, category, cost_per_day, id=None):
        self.location = location
        self.category = category
        self.cost_per_day = cost_per_day
        self.id = id

    def __repr__(self):
        return f"<Destination{self.id}: {self.location}, {self.category}, {self.cost_per_day}"

    @property
    def location(self):
        return self._location 

    @location.setter
    def location(self, location):
        if not isinstance(location, str):
            raise TypeError("location must be in string format")
        elif not re.match(r"^[a-zA-Z]+(?:\s[a-zA-Z]+)?$", location):
            raise ValueError("Please fill out location")
        self._location = location

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("category must be in string format")
        elif category not in ("nature", "historic", "food", "excursion"):
            raise ValueError(
                "category must be one of the options of: nature, history, food, or excursion"
            )
        self._category = category

    @property
    def cost_per_day(self):
        return self._cost_per_day

    @cost_per_day.setter
    def cost_per_day(self, cost_per_day):
        if not isinstance(cost_per_day, str):
            raise TypeError("cost_per_day must be in float format")
        elif re.match(r"[0-9]+\.[0-9]$", str(cost_per_day)):
            self._cost_per_day = str(cost_per_day) + '0'
        elif not re.match(r"[0-9]+\.[0-9]{2}", str(cost_per_day)):
            raise ValueError("cost_per_day must be in the format of float with 2 decimal places")
        else:
            self._cost_per_day = cost_per_day

    # Association Methods

    def bookings(self):
        CURSOR.execute(
            """
            SELECT * FROM bookings
            WHERE destination_id = ?
        """,
            (self.id,),
        )
        rows = CURSOR.fetchall()
        return [Booking(row[1], row[2], row[3], row[0]) for row in rows]

    # Utility ORM Methods

    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                    CREATE TABLE IF NOT EXISTS destinations (
                        id INTEGER PRIMARY KEY,
                        location TEXT, 
                        category TEXT,
                        cost_per_day TEXT
                    );
                """
            )
            CONN.commit()
        except Exception as e:
            return e

    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute(
                """
                DROP TABLE IF EXISTS destinations;
            """
            )
            CONN.commit()
        except Exception as e:
            return e

    @classmethod
    def create(cls,location, category, cost_per_day):
        new_destination = cls(location, category, cost_per_day)
        new_destination.save()
        return new_destination

    @classmethod
    def new_from_db(cls):
        CURSOR.execute(
            """ 
                SELECT  * FROM destination
                ORDER BY id DESC
                LIMIT 1;
            """
        )
        row= CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0])
    
    @classmethod
    def get_all(cls):
        CURSOR.execute(
            """ 
                SELECT * FROM destinations;
            """
        )
        rows= CURSOR.fetchall()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]
    
    @classmethod
    def find_by_location(cls, location): 
        CURSOR.execute(
            """" 
                SELECT * FROM destinations
                WHERE id is ?;
            """,
                (location,),
        )
        row = CURSOR.fetchone()
        return cls(row[1], row[2], row[3], row[0]) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        CURSOR.execute(
            """" 
                SELECT * FROM destination
                WHERE id is ?;
            """,
                (id,),
        )
        row = CURSOR.fetchone()
        return cls(row[1],  row[2], row[3], row[0]) if row else None
    
    @classmethod
    def find_or_create_by(cls, location, category, cost_per_day):
        return cls.find_by_location(location) or cls.create(
            location, category, cost_per_day
        )
        
    # Utility ORM Instance Methods
    def save(self):
        CURSOR.execute(
            """ 
                INSERT INTO destinations (location, category, cost_per_day)
                VALUES (?, ?, ?);
            """,
                (self.location, self.category, self.cost_per_day),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        return self
    
    def update(self):
        CURSOR.execute(
            """" 
                UPDATE destinations
                SET location = ?, category = ?, cost_per_day = ?
                WHERE id = ?
            """, 
                (self.location, self.category, self.cost_per_day, self.id),
        )
        CONN.commit()
        type(self).all[self] = self
        return self
    
    def delete(self):
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
