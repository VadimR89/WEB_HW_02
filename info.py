from datetime import datetime as dt
import re
from abc import ABC, abstractmethod

class Record:

    def __init__(self, name, phones=None, birthday=None, email=None, status=None, note=None):
        self.name = Name(name)
        self.phones = Phone(phones)
        self.birthday = Birthday(birthday)
        self.email = Email(email)
        self.status = Status(status)
        self.note = Note(note)

    def days_to_birthday(self):
        if self.birthday:
            current_datetime = dt.now()
            birthday = self.birthday.__getitem__()
            birthday = birthday.replace(year=current_datetime.year)
            if birthday >= current_datetime:
                result = birthday - current_datetime
            else:
                birthday = birthday.replace(year=current_datetime.year + 1)
                result = birthday - current_datetime
            return result.days
        return None

class Field(ABC):

    @abstractmethod
    def __getitem__(self):
        pass

    def __str__(self):
        return str(self.__getitem__())

class Name(Field):
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value

class Phone(Field):
    def __init__(self, value=None):
        if value is None:
            value = input("Phones(+48......... or +38..........) (multiple phones can be added with space between them. +48 pattern has 9 symbols after code): ")
        self.value = []
        for number in value.split(' '):
            if re.match('^\+48\d{9}$', number) or re.match('^\\+38\d{10}$', number) or number == '':
                self.value.append(number)
            else:
                raise ValueError('Incorrect phone number format! Please provide correct phone number format.')

class Birthday(Field):
    def __init__(self, value=None):
        if value is None:
            value = input("Birthday date(dd/mm/YYYY): ")
        if re.match('^\d{2}/\d{2}/\d{4}$', value):
            self.value = dt.strptime(value.strip(), "%d/%m/%Y")
        elif value == '':
            self.value = None
        else:
            raise ValueError('Incorrect date! Please provide correct date format.')

class Email(Field):
    def __init__(self, value=None):
        if value is None:
            value = input("Email: ")
        if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', value) or value == '':
            self.value = value
        else:
            raise ValueError('Incorrect email! Please provide correct email.')

class Status(Field):
    def __init__(self, value=None):
        self.status_types = ['', 'family', 'friend', 'work']
        if value is None:
            value = input("Type of relationship (family, friend, work): ")
        if value in self.status_types:
            self.value = value
        else:
            raise ValueError('There is no such status!')

class Note(Field):
    def __init__(self, value):
        self.value = value