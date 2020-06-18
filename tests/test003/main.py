'''
function annotation ->

how it work
'''


class Dog():
    def __init__(self) -> None:
        super().__init__()

    def bark(self):
        print('barlk')


def command() -> Dog:
    pass

a = command()
a.bark()