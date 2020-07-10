import test031.module as module

# Underscores, dundersand more

module.external_func()
module._iternal_func()


class Test:
    def __init__(self) -> None:
        self.foo = 11
        self._bar = 23
        self.__baz = 23


if __name__ == '__main__':
    # test = Test()
    test = Test.__init__(Test())

    print(dir(test))
