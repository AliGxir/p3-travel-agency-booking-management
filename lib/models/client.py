from models.__init__ import CURSOR, CONN
import re


class Client:
    all = {}

    def __init__(self, name, start_date, end_date, category):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.category = category
        self.id = self

    def __repr__(self):
        return f"<Client {self.id}: {self.name}, {self.start_date}, {self.end_date}, {self.category}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
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
        self._end_date = end_date

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
                        start_date TEXT, 
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
    def create(cls, name, start_date, end_date, category):
        new_client = cls(name, start_date, end_date, category)
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
    def find_or_create_by(cls, name, start_date, end_date, category):
        return cls.find_by_name(name) or cls.create(
            name, start_date, end_date, category
        )
        
    