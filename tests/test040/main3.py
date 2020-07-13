# Instance, Class, and Static Methods
# Demystified


class MyClass:

    def method(self):
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


if __name__ == '__main__':
    my_class = MyClass()

    print(my_class.method())
    print(my_class.class_method())

    print(MyClass.method(my_class))
    print(my_class.class_method())

