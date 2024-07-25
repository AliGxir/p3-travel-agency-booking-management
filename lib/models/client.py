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
        