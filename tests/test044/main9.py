class AlwaysEquals:
    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)


if __name__ == '__main__':
    print(AlwaysEquals() == AlwaysEquals())
    print(AlwaysEquals() == 40)
    print(40 == AlwaysEquals)

    objects = [AlwaysEquals(),
               AlwaysEquals(),
               AlwaysEquals()]
    print([hash(obj) for obj in objects])