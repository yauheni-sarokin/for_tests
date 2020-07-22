# typing named tuple

from typing import NamedTuple


class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

if __name__ == '__main__':
    car = Car('red', 3812.4, True)
    print(car)
    print(car.mileage)