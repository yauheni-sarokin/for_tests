from abc import ABC, abstractmethod

'''
Учим питон с Антоном
'''


class Animal(ABC):

    def __init__(self, name: str) -> None:
        print(f'initialization of {self.__class__}]')
        self.__name = name

    @property
    def name(self):
        return self.__name

    def say_your_name(self):
        print(f'my name is {self.__name}')

    @abstractmethod
    def start_speaking(self):
        pass


class Dog(Animal):
    def start_speaking(self):
        print('woof')


class Cat(Animal):
    def start_speaking(self):
        print('meow')

class Wolf(Animal):

    def start_speaking(self):
        print('auuuuu')


def make_animal_speak(any_animal: Animal):
    any_animal.say_your_name()
    any_animal.start_speaking()
    any_animal.start_speaking()
    any_animal.start_speaking()

if __name__ == '__main__':
    dog = Dog('Barbos')
    cat = Cat('Murzik')
    wolf = Wolf('Seriy')

    make_animal_speak(wolf)


