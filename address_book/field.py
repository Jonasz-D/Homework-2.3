from abc import ABC, abstractmethod

class AbsField(ABC):
    @abstractmethod
    def value(self):
        pass

class Field(AbsField):
    def __init__(self, input_value = None):
        self.internal_value = None
        self.value = input_value

    @property
    def value(self):
        return self.internal_value
    
    @value.setter
    def value(self, input_value):
        self.internal_value = input_value


