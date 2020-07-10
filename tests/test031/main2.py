_MangledGlobal__mangled = 23


class MangledGlobal:

    def test(self):
        return __mangled


if __name__ == '__main__':
    print(MangledGlobal().test())

    print(dir(MangledGlobal().test()))
