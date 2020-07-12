# abstract base classes


from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def bar(self):
        pass

    def foo(self):
        pass


if __name__ == '__main__':
    concrete = Concrete()

    print(issubclass(concrete.__class__, Base))

    c = concrete.__class__()
