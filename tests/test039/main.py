# named tuples

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

if __name__ == '__main__':
    my_car = Car('red', 3819.3)
    print(my_car.color)
    print(*my_car)