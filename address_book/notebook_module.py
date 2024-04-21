from .field import Field
from collections import UserDict
import re


class Notebook(UserDict):
    num_of_notes = 0

    def add_note(self, note, tags):
        try:
            Notebook.num_of_notes += 1
            while True:
                if Notebook.num_of_notes in self.data.keys():
                    Notebook.num_of_notes += 1
                else:
                    break
            self.num_of_note = Notebook.num_of_notes
            self.data[self.num_of_note] = [Note(note).internal_value, Tags(tags).internal_value]
            return True
        
        except ValueError as e:
            print(e)
            return False
        
    def show_notes(self):
        width = 154
        all_notes = ''
        all_notes += "\n+" + "-" * width + "+\n"
        all_notes += '|{:^20}|{:^100}|{:^32}|\n'.format("NUMBER OF NOTE", "NOTE", "TAGS")
        all_notes += "+" + "-" * width + "+\n"
        for num_of_note, note_and_tags in self.data.items():
            note = note_and_tags[0]
            tags = note_and_tags[1]
            str_tags = ''
            for tag in tags:
                str_tags += f'{tag}; '
            all_notes += f'|{str(num_of_note):^20}|{str(note):^100}|{str_tags:^32}|\n'
        all_notes += "+" + "-" * width + "+"
        return all_notes
    
    def search_note_by_tags(self, searched_tags):
        width = 154
        finded_notes_data = []
        searched_tags = Tags(searched_tags).internal_value
        finded_notes = ''
        finded_notes += "\n+" + "-" * width + "+\n"
        finded_notes += '|{:^20}|{:^100}|{:^32}|\n'.format("NUMBER OF NOTE", "NOTE", "TAGS")
        finded_notes += "+" + "-" * width + "+\n"
        for num_of_note, note_and_tags in self.data.items():
            note = note_and_tags[0]
            tags = note_and_tags[1]
            
            if searched_tags <= tags:
                str_tags = ''
                for tag in tags:
                    str_tags += f'{tag}; '
                finded_notes_data.append(num_of_note)
                finded_notes += f'|{str(num_of_note):^20}|{str(note):^100}|{str_tags:^32}|\n'
        
        finded_notes += "+" + "-" * width + "+"
        if finded_notes_data == []:
            return f'Notes not find'
        else:
            return finded_notes
    
    def edit_note(self, num_of_note, note, tags):
        if num_of_note not in str(self.data.keys()):
            return ('Number of note doesn\'t exists')
        else:
            try:
                self.data[int(num_of_note)] = [Note(note).internal_value, Tags(tags).internal_value]
                return 'Note has been changed'
            
            except ValueError as e:
                return e

            
    def remove_note(self, num_of_note):
        if num_of_note == 'all':
            Notebook.num_of_notes = 0
            self.data.clear()
            return 'Note(s) has been removed'
    
        elif num_of_note not in str(self.data.keys()):
            return 'Number of note doesn\'t exists'

        else:
            self.data.pop(int(num_of_note))
            return 'Note(s) has been removed'

    def remove_all_notes(self):
        self.note = ''

    def change_notebook(self, note):
        self.note = Notebook(note).value
    
class Note(Field):
    @Field.value.setter
    def value(self, note):
        if note == '':
            raise ValueError("Note must include any characters")
        self.internal_value = note

class Tags(Field):
    @Field.value.setter
    def value(self, tags:str):
        tags = tags.lower()
        tags = re.split(r'[^0-9a-z]', tags)
        tags = set(filter(lambda tag: tag.isalnum(), tags))
        self.internal_value = tags