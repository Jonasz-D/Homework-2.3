from .addressbook_module import *
from .files_utilities import *
from .sorting_module import main_sorting_folder
from datetime import datetime
import pickle
import os
from abc import ABC, abstractmethod

address_book = load_from_file()

def send_msg(msg):
    print(msg)

def input_value(msg):
    input_value = input(msg).lower()
    return input_value

class FunctionsPattern(ABC):
    @abstractmethod
    def function_logic(self):
        pass


class AddContact(FunctionsPattern): 
    def function_logic(self): 
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)   
        if name in address_book.contacts:
            msg = "A contact with this name already exists."
            send_msg(msg)
        else:
            try:
                address_book.contacts[name] = Contact(name)
            except Exception as e:
                msg = e
                send_msg(msg)
            if name in address_book.contacts:
                    msg = f"Contact {name} was added."
                    send_msg(msg)

class DeleteContact(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname you'd like to delete: "
        name = input_value(msg)

        if name in address_book.contacts:
            address_book.contacts.pop(name)
            msg = f'Contact {name} deleted.'
            send_msg(msg)
        else:
            msg = f'There is no contact {name}'
            send_msg(msg)

class AddPhone(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if not name in address_book.contacts:
            msg = f'There is no contact {name}'
            send_msg(msg)
            return
            
        if address_book.contacts[name].phone.value:
            msg = f'Contact have a phone number already. To change an existing number use "change phone" command.'
            send_msg(msg)
            return

        msg = "Enter phone number: "
        phone = input_value(msg)            
        try:
            address_book.contacts[name].add_phone(phone)
            if address_book.contacts[name].phone.value:
                msg = f"{phone} was added to contact {name}."
                send_msg(msg)
        except:
            return 

class ChangePhoneNum(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if not name in address_book.contacts:
            msg = f'There is no contact {name}'
            send_msg(msg)
            return
        if not address_book.contacts[name].phone.value:
            msg = f"Contact {name} doesnt have a phone number yet. However we can proceed."

        msg = "Enter the new phone number: "
        new_phone = input_value(msg)
        try:
            address_book.contacts[name].add_phone(new_phone)
            if address_book.contacts[name].phone.value == new_phone[0:3] + '-' + new_phone[3:6] + '-' + new_phone[6:]:
                msg = f"Number was changed for contact {name}."
                send_msg(msg)
        except:
            return

class DeletePhone(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if name in address_book.contacts:
            address_book.contacts[name].delete_phone()
            msg = f"Phone number deleted for {name}."
            send_msg(msg)
        else:
            msg = "Contact not found."
            send_msg(msg)

class AddEmail(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if not name in address_book.contacts:
            msg = f'There is no contact {name}'
            send_msg(msg)
            return
        if address_book.contacts[name].email.value:
            msg = f'Contact have an email already. To change an existing email use "change email" command.'
            send_msg(msg)
            return
        msg = "Enter the email: "
        email = input_value(msg)
        try:
            address_book.contacts[name].add_email(email)
            if address_book.contacts[name].email.value:
                msg = f"{email} was added to contact {name}."
                send_msg(msg)
        except:
            return
    
class ChangeEmail(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if not name in address_book.contacts:
            msg = f'There is no contact {name}'
            send_msg(msg)
            return
        if not address_book.contacts[name].email.value:
            msg = f"Contact {name} doesnt have a email yet. However we can proceed."
            send_msg(msg)
        msg = "Enter the email: "
        email = input_value(msg)
        try:
            address_book.contacts[name].add_email(email)
            if address_book.contacts[name].email.value == email:
                msg = f"{email} was changed for contact {name}."
                send_msg(msg)
        except:
            return
    
class DeleteEmail(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if not name in address_book.contacts:
            msg = f'There is no contact {name}'
            send_msg(msg)
            return
        address_book.contacts[name].remove_email()
        msg = f'Email deleted'
        send_msg(msg)

def get_valid_date_input(prompt):
    while True:
        try:
            msg = "\n" + prompt + " (year): "
            year = int(input_value(msg))
            msg = prompt + " (month): "
            month = int(input_value(msg))
            msg = prompt + " (day): "
            day = int(input_value(msg))

            date = datetime(year, month, day).date()
            today = datetime.now().date()
            if date > today:
                msg = "\nInvalid date. Please enter a date not further into the future than today."
                send_msg(msg)
            else:
                return date.strftime('%Y-%m-%d')
        except ValueError:
            msg = "\nInvalid date. Please enter a valid date."
            send_msg(msg)

class SetBirthday(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if name in address_book.contacts:
            if address_book.contacts[name].birthday.value:
                msg = f"\nContact {name.title()} already has a birthday date set to {address_book.contacts[name].birthday.value}."
                send_msg(msg)
                msg = "Do you want to edit the birthday date? (yes/no): "
                edit_birthday = input_value(msg)
                if edit_birthday == "yes":
                    birthday_to_add = get_valid_date_input("Enter the new birthday date")
                    address_book.contacts[name].add_birthday(birthday_to_add)
                    msg = f"\nNew birthday date ({birthday_to_add}) added to contact {name.title()}"
                    send_msg(msg)
                else:
                    msg = f"\nBirthday date for {name.title()} remains unchanged."
                    send_msg(msg)
            else:
                birthday_to_add = get_valid_date_input("Enter the contact's birthday date")
                address_book.contacts[name].add_birthday(birthday_to_add)
                msg = f"\nBirthday date ({birthday_to_add}) added to contact {name.title()}"
                send_msg(msg)
        else:
            msg = "\nContact not found."
            send_msg(msg)

class DaysToBirthday(FunctionsPattern):
    def function_logic(self):   
        width = 123
        msg = "\n+" + "-" * width + "+"

        msg += '\n|{:^30}|{:^30}|{:^30}|{:^30}|'.format("NAME", "BIRTHDAY", "DAYS TO BIRTHDAY", "UPCOMING")

        msg += "\n+" + "-" * width + "+"

        
        for contact_name in address_book.contacts:
            contact = address_book.contacts[contact_name]
            if contact.birthday.value and contact.days_to_birthday < 31:
                format_value = lambda x: x if x is not None else "---"
                msg += '\n|{:^30}'.format(format_value(contact.name.value.title()))            
                msg += '|{:^30}'.format(format_value(contact.birthday.value)) 
                msg += '|{:^30}'.format(format_value(contact.days_to_birthday))
                days_to_birthday = contact.days_to_birthday
                
                if contact.birthday.value:
                    birthday_date = datetime.strptime(contact.birthday.value, "%Y-%m-%d")
                    today = datetime.today()
                    next_birthday = datetime(today.year, birthday_date.month, birthday_date.day)
                    
                    if today > next_birthday:
                        next_birthday = datetime(today.year + 1, birthday_date.month, birthday_date.day)
                    
                    days_from_beginning_of_week = (today.weekday() - 7) % 7
                    
                    if days_to_birthday == 0:
                        msg += '|{:^30}|'.format("Today")
                    elif days_to_birthday == 1:
                        msg += '|{:^30}|'.format("Tomorrow")
                    elif days_to_birthday < 7 - days_from_beginning_of_week:
                        msg += '|{:^30}|'.format("This week")
                    elif days_to_birthday < 14 - days_from_beginning_of_week:
                        msg += '|{:^30}|'.format("Next week")
                    elif next_birthday.month == today.month:
                        msg += '|{:^30}|'.format("This month")
                    elif (today.month + 1) % 12 == next_birthday.month % 12:
                        msg += '|{:^30}|'.format("Next month")
                    else:
                        msg += '|{:^30}|'.format("---")
                else:
                    msg += '|{:^30}|'.format("---")
                
        msg += "\n+" + "-" * width + "+\n"
        send_msg(msg)

class AddAddress(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if not name in address_book.contacts:
            msg = f'There is no contact {name}'
            send_msg(msg)
            return
        msg = "City: "
        city = input_value(msg)
        msg = "Street: "
        street = input_value(msg)
        msg = "House and flat number: "
        number = input_value(msg)
        address = city + ' ' + street + ' ' + number
        try:
            address_book.contacts[name].add_address(address.title())
            if address_book.contacts[name].address.value:
                msg = f"{address} was added to contact {name}."
                send_msg(msg)
        except:
            return
    
class ChangeAddress(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if not name in address_book.contacts:
            msg = f'There is no contact {name}'
            send_msg(msg)
            return
        if not address_book.contacts[name].address.value:
            msg = f"Contact {name} doesnt have a email yet. However we can proceed."
            send_msg(msg)
        msg = "City: "
        city = input_value(msg)
        msg = "Street: "
        street = input_value(msg)
        msg = "House and flat number: "
        number = input_value(msg)
        address = city + ' ' + street + ' ' + number
        try:
            address_book.contacts[name].add_address(address.title())
            if address_book.contacts[name].address.value == address.title():
                msg = f"{address} was changed for contact {name}."
                send_msg(msg)
        except:
            return
    
class DeleteAddress(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        name = input_value(msg)
        if not name in address_book.contacts:
            msg = f'There is no contact {name}'
            send_msg(msg)
            return
        address_book.contacts[name].remove_address()
        msg = f'Address deleted'
        send_msg(msg)

class AddNote(FunctionsPattern):
    def function_logic(self): 
        msg = "Enter the note text: "
        note = input_value(msg)
        msg = "Enter tags: "
        tags = input_value(msg)
        address_book.notebook.add_note(note, tags)

class EditNote(FunctionsPattern):
    def function_logic(self): 
        if not address_book.notebook.data:
            msg = 'Notebook is empty'
            send_msg(msg)
        else:
            msg = f'{address_book.notebook.show_notes()}'
            send_msg(msg)
            msg = f'Enter number of note: '
            num_of_note = input_value(msg)
            msg = 'Enter new note text: ' 
            note_text = input_value(msg)
            msg = "Enter new tags: "
            tags = input_value(msg)
            msg = address_book.notebook.edit_note(num_of_note, note_text, tags)
            send_msg(msg)

class RemoveNote(FunctionsPattern):
    def function_logic(self): 
        if not address_book.notebook.data:
            msg = 'Notebook is empty'
            send_msg(msg)
        else:
            msg = f'{address_book.notebook.show_notes()}'
            send_msg(msg)
            msg = 'Enter number of note or write "all" to remove all notes: '
            num_of_note = input_value(msg)
            msg = address_book.notebook.remove_note(num_of_note)
            send_msg(msg)

class ShowNotes(FunctionsPattern):
    def function_logic(self): 
        msg = f'List of notes: \n {address_book.notebook.show_notes()}'
        send_msg(msg)

class SearchNoteByTags(FunctionsPattern):
    def function_logic(self): 
        msg = "Enter tags: "
        searched_tags = input_value(msg)
        msg = address_book.notebook.search_note_by_tags(searched_tags)
        send_msg(msg)

class ShowAll(FunctionsPattern):
    def function_logic(self): 
        width = 154
        msg = "\n+" + "-" * width + "+"
        send_msg(msg)
        msg = '|{:^30}|{:^13}|{:^35}|{:^12}|{:^60}|'.format("NAME", "PHONE", "EMAIL", "BIRTHDAY", "ADDRESS")
        send_msg(msg)
        msg = "+" + "-" * width + "+"
        send_msg(msg)
        for contact_name in address_book.contacts:
            contact = address_book.contacts[contact_name]
            format_value = lambda x: x if x is not None else "---"
            msg = '|{:^30}'.format(format_value(contact.name.value.title()))
            msg += '|{:^13}'.format(format_value(contact.phone.value))
            msg += '|{:^35}'.format(format_value(contact.email.value))
            msg += '|{:^12}'.format(format_value(contact.birthday.value))
            msg += '|{:^60}|'.format(format_value(contact.address.value))
            send_msg(msg)
        msg = "+" + "-" * width + "+\n"
        send_msg(msg)

class FindContact(FunctionsPattern):
    def function_logic(self):   
        msg = "Enter the contact's name and surname: "
        search_phrase = input_value(msg)
        width = 154
        msg = "\n+" + "-" * width + "+"
        send_msg(msg)
        msg = '|{:^30}|{:^13}|{:^35}|{:^12}|{:^60}|'.format("NAME", "PHONE", "EMAIL", "BIRTHDAY", "ADDRESS")
        send_msg(msg)
        msg = "+" + "-" * width + "+"
        send_msg(msg)
        found = False
        for name, contact in address_book.contacts.items():
            if search_phrase in name:
                found = True
                format_value = lambda x: x if x is not None else "---"
                msg = '|{:^30}'.format(format_value(contact.name.value.title()))
                msg += '|{:^13}'.format(format_value(contact.phone.value))
                msg += '|{:^35}'.format(format_value(contact.email.value))
                msg += '|{:^12}'.format(format_value(contact.birthday.value))
                msg += '|{:^60}|'.format(format_value(contact.address.value))
                send_msg(msg)
        if not found:
            msg = "|{:^154}|".format("\"" + search_phrase + "\" not present in the address book.")
            send_msg(msg)
        msg = "+" + "-" * width + "+\n"
        send_msg(msg)

class SortFolder(FunctionsPattern):
    def function_logic(self):   
        current_path = os.getcwd()
        msg = "Enter path to folder that should be sorted: "
        path_to_folder = input_value(msg)
        main_sorting_folder(path_to_folder)
        os.chdir(current_path)

class SaveToFile(FunctionsPattern):
    def function_logic(self):   
        dir_path = os.path.dirname(os.path.realpath(__file__))
        save_path = os.path.join(dir_path, "data_save.bin")
        with open(save_path, "wb") as fh:
            pickle.dump(address_book, fh)
        msg = 'File has been saved'
        send_msg(msg)

class EndProgram(FunctionsPattern):
    def function_logic(self): 
        save_to_file = SaveToFile().function_logic()
        msg = 'Goodbye'
        send_msg(msg)

class AcceptedCommands(FunctionsPattern):
    def function_logic(self, commands): 
        self.commands = commands
        col = 4
        width = 20 * col + col - 1
        c = 1
        msg = "\n+" + "-" * width + "+"
        for command in self.commands.keys():
            if c == 1:
                msg += "\n|{:^20}".format(command)
                c += 1
            elif c < col:            
                msg += "|{:^20}".format(command)
                c += 1
            else:
                msg += "|{:^20}|".format(command)
                c = 1
        msg += "\n+" + "-" * width + "+\n"
        send_msg(msg)

class UnknownCommand(FunctionsPattern):
    def function_logic(self): 
        msg = "\nUnknown command! Please type 'help' to get the list of available commands."
        send_msg(msg)



