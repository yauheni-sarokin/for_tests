# Class vs Instance Variable Pitfalls


class Dog:
    num_legs = 4  # <- Class variable

    def __init__(self, name):
        self.name = name  # <- Instance variable


if __name__ == '__main__':
    print(Dog.num_legs)
    dog = Dog('Jack')
    print(dog.num_legs)

    dog.num_legs = 6
    print(dog.num_legs)
    print(Dog.num_legs)
