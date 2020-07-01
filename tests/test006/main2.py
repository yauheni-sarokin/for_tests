'''
Getter setter OOP way
Property
'''


class Property:
    def __init__(self, var) -> None:
        self.__a = var

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2


if __name__ == "__main__":
    obj = Property(123)

    print(obj.a)