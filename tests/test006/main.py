"""
property decorator, setter
pythonic way
"""

#pythonic way
class SampleClass:
    def __init__(self, a) -> None:
        self.__a = a
        self.b = a

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

if __name__ == '__main__':
    some_class = SampleClass(123)
    print(some_class.b)