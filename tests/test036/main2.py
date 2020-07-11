# String conversion


class Car:

    def __init__(self, color, mileage) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f'a {self.color} car'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(' \
               f'{self.color!r}, {self.mileage!r})'


