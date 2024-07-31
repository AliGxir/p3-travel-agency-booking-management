from models.__init__ import CURSOR, CONN
import re


class Client:
    all = {}

    def __init__(self, name, start_date, end_date, category, destination, id=None):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.category = category
        self.destination = destination
        self.id = id

    def __repr__(self):
        return f"<Client {self.id}: {self.name}, {self.start_date}, {self.end_date}, {self.category}, {self.destination}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be in string format")
        elif not re.match(r"^[a-zA-Z]", name):
            raise ValueError("Please fill out name")
        self._name = name

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
        elif self.start_date > end_date:
            raise ValueError("start_date must be before end_date")
        self._end_date = end_date

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("category must be in string format")
        elif not ("nature", "historic", "food", "excursion"):
            raise ValueError(
                "category must be one of the options of: nature, historic, food, or excursion"
            )
        self._category = category

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination):
        if not isinstance(destination, str):
            raise TypeError("destination must be in string format")
        elif not (
            "Oahu",
            "Rome",
            "Paris",
            "Tokyo",
            "Amsterdam",
            "Singapore",
            "Bangkok",
            "Hong Kong",
            "New York",
            "San Francisco",
        ):
            raise ValueError(
                "destination must be one of the options of: Oahu, Rome, Paris, Tokyo, Amsterdam, Singapore, Bangkok, Hong Kong, New York, San Francisco"
            )
        self._destination = destination

    # Association Methods
    def bookings(self):
        try:
            CURSOR.execute(
                """
                SELECT * FROM bookings
                WHERE client_id = ?
            """,
                (self.id,),
            )
            rows = CURSOR.fetchall()
        except Exception as e:
            CONN.rollback()
            return e
        return [
            Booking(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows
        ]

    # Utility ORM Methods
    @classmethod
    def create_table(cls):
        try:
            CURSOR.execute(
                """
                    CREATE TABLE IF NOT EXISTS clients (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        start_date TEXT, 
                        end_date TEXT, 
                        category TEXT,
                        destination TEXT
                    );
                """
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback
            return e

    @classmethod
    def drop_table(cls):
        try:
            CURSOR.execute(
                """
                DROP TABLE IF EXISTS clients;
            """
            )
            CONN.commit()
        except Exception as e:
            CONN.rollback
            return e

    @classmethod
    def create(cls, name, start_date, end_date, category, destination):
        try:
            new_client = cls(name, start_date, end_date, category, destination)
            new_client.save()
        except Exception as e:
            CONN.rollback
            return e
        return new_client

    @classmethod
    def new_from_db(cls):
        try:
            CURSOR.execute(
                """ 
                    SELECT  * FROM clients
                    ORDER BY id DESC
                    LIMIT 1;
                """
            )
            row = CURSOR.fetchone()
        except Exception as e:
            CONN.rollback
            return e
        return cls(row[1], row[2], row[3], row[4], row[5], row[0])

    @classmethod
    def get_all(cls):
        try:
            CURSOR.execute(
                """
                    SELECT * FROM clients;
                """
            )
            rows = CURSOR.fetchall()
        except Exception as e:
            CONN.rollback
            return e
        return [cls(row[1], row[2], row[3], row[4], row[5], row[0]) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        try:
            CURSOR.execute(
                """ 
                    SELECT * FROM clients
                    WHERE name is ?;
                """,
                (name,),
            )
            row = CURSOR.fetchone()
        except Exception as e:
            CONN.rollback
            return e
        return cls(row[1], row[2], row[3], row[4], row[5], row[0]) if row else None

    @classmethod
    def find_by_id(cls, id):
        try:
            CURSOR.execute(
                """ 
                    SELECT * FROM clients
                    WHERE id is ?;
                """,
                (id,),
            )
            row = CURSOR.fetchone()
        except Exception as e:
            CONN.rollback
            return e
        return cls(row[1], row[2], row[3], row[4], row[5], row[0]) if row else None

    # Utility ORM Instance Methods
    def save(self):
        try:
            CURSOR.execute(
                """ 
                    INSERT INTO clients (name, start_date, end_date, category, destination)
                    VALUES (?, ?, ?, ?, ?);
                """,
                (
                    self.name,
                    self.start_date,
                    self.end_date,
                    self.category,
                    self.destination,
                ),
            )
            CONN.commit()
            self.id = CURSOR.lastrowid
            type(self).all[self.id] = self
        except Exception as e:
            CONN.rollback
            return e
        return self

    def update(self):
        try:
            CURSOR.execute(
                """
                UPDATE clients
                SET name = ?, start_date = ?, end_date = ?, category = ?, destination = ?
                WHERE id = ?
            """,
                (
                    self.name,
                    self.start_date,
                    self.end_date,
                    self.category,
                    self.destination,
                    self.id,
                ),
            )
            CONN.commit()
            type(self).all[self] = self
        except Exception as e:
            return e
        return self

    def delete(self):
        try:
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
        except Exception as e:
            return e
        return self

from models.booking import Booking
