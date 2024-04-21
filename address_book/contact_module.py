import re
from datetime import datetime
from .field import Field


class Contact():
    def __init__(self, name, phone=None, address=None, email=None, birthday=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.address = Address(address)
        self.email = Email(email)
        self.birthday = Birthday(birthday)
        
    def add_phone(self, phone):
        self.phone = Phone(phone)       
        
    def delete_phone(self, phone=None):
        self.phone = Phone(phone)   

    def change_phone(self, new_phone):
        self.phone = Phone(new_phone) 
        
    def add_email(self, email):
        self.email = Email(email)

    def remove_email(self, email=None):
        self.email = Email(email)
        
    def add_address(self, address):
        self.address = Address(address)

    def remove_address(self, address = None):
        self.address = Address(address)
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    @property
    def days_to_birthday(self):
        if self.birthday.value:
            today = datetime.today()
            birthday_date = datetime.strptime(self.birthday.value, "%Y-%m-%d")
            upcoming_birthday_date = datetime(today.year, birthday_date.month, birthday_date.day)
            if today.date() == upcoming_birthday_date.date():
                return 0
            elif today > upcoming_birthday_date:
                upcoming_birthday_date = datetime(today.year + 1, birthday_date.month, birthday_date.day)
            delta = upcoming_birthday_date - today
            return delta.days + 1
        else:
            return None

class Name(Field):
    @Field.value.setter
    def value (self, name):
        if not name:
            raise ValueError("Name is a mandatory field and cannot be empty!")       
        self.internal_value = name.lower()

class Phone(Field):
    @Field.value.setter
    def value(self, number):
        if number:
            number = number.strip()
            if not number.isdigit() or len(number) != 9:
                return ("Number must be 9 digits long and contain digits only.")
            self.internal_value = number[0:3]+'-'+number[3:6]+'-'+number[6:]

class Address(Field):
    @Field.value.setter
    def value(self, address: str):
        if address:
            if len(address) > 56:
                raise ValueError('Address should not exceed 56 characters.')
            address = address.title()
        self.internal_value = address

class Email(Field): 
    @Field.value.setter
    def value(self, email):
        if email:
            """Check email format"""
            patern_email = r"^([A-Za-z0-9]+ |[A-Za-z0-9][A-Za-z0-9\.\_]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9\_\-]+[A-Za-z0-9])\.([a-z]{,3}|[a-z]{3}\.[a-z]{2})$"
            result = re.findall(patern_email,email)
            if result == []:
                raise ValueError('Wrong email format!')
        self.internal_value = email

class Birthday(Field):
    @Field.value.setter
    def value(self, input_value: str):
        self.internal_value = input_value