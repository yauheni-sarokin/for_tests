# factory
import math


class Pizza:

    def __init__(self, radius, ingredients) -> None:
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self) -> str:
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

    def are(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 ** math.pi


if __name__ == '__main__':
    margherita = Pizza.margherita()
    print(margherita)
