from .functions import *

class FacadeHandler:
    def __init__(self, commands):
        self.commands = commands

    def function_runner(self, command):
        if command == 'help':
            return self.commands[command](self.commands)
        elif command in self.commands:
            return self.commands[command]  
        else:
            unknown_command = UnknownCommand().function_logic()
            return unknown_command
        
def my_func(creator:FunctionsPattern):
    func = creator.function_logic
    return func

def input_parser():
    """Functions runs in a while loop, takes input from user and returns apropiate functions
    """
    commands = {
    'add contact': my_func(AddContact()),
    'delete contact': my_func(DeleteContact()),
    'add phone': my_func(AddPhone()),
    'change phone': my_func(ChangePhoneNum()),
    'delete phone': my_func(DeletePhone()),
    'add email': my_func(AddEmail()),
    'change email': my_func(ChangeEmail()),
    'delete email': my_func(DeleteEmail()),
    'add birthday' : my_func(SetBirthday()),
    'birthday': my_func(DaysToBirthday()),
    'add address': my_func(AddAddress()),
    'change address': my_func(ChangeAddress()),
    'delete address': my_func(DeleteAddress()),
    'add note': my_func(AddNote()),
    'edit note': my_func(EditNote()),
    'delete note': my_func(RemoveNote()),
    'show notes':my_func(ShowNotes()),
    'find note': my_func(SearchNoteByTags()),
    'show all': my_func(ShowAll()),
    'find contact' : my_func(FindContact()),
    'sort folder': my_func(SortFolder()),
    'save': my_func(SaveToFile()),
    'exit': my_func(EndProgram()),
    'help': my_func(AcceptedCommands()), 
    }
    return commands

facade_handler = FacadeHandler(input_parser())
      