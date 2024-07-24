from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def voice(self):
        pass

class Cat(Animals):
    def __init__(self, age=0):
        self.age = age
    def voice(self):
        print('Meow')

test = Cat()
test.voice()
