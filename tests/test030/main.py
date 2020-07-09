'''
Учим питон с Антоном
'''


class Animal:
    pass


class Dog:
    pass


class Cat:

    def __init__(self, name: str) -> None:
        """
        Here initialize cat with name
        :param name: Write his name
        """
        self.__name = name

    def meow(self) -> None:
        print('meeow')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        assert isinstance(value, str), 'NAME IS NOT STRING!!!'
        self.__name = value


if __name__ == '__main__':
    cat = Cat('Barsik')
    cat.meow()
    # cat.say_name()
    cat.name = 123
    name = cat.name
    print(name)

    cat2 = Cat('Fufel')
    cat.meow()
    # cat2.cat_name = 'Bus'
    # cat2.say_name()