'''
Abstract base classes
'''
#the infrastructure for defining Abstract Base Classes (ABCs).
from abc import ABC, abstractmethod


class AbstractClassExample(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        pass

class DoAdd42(AbstractClassExample):

    def do_something(self):
        return self.value + 42

class DoMu142(AbstractClassExample):

    def do_something(self):
        return self.value * 42

x = DoAdd42(10)
y = DoMu142(10)

print(x.do_something())
print(y.do_something())

