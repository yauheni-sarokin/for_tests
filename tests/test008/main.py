"""
Singleton
Наивный Одиночка (небезопасный в многопоточной среде)
#todo Прочитать что такое мета класс, cls *args
"""

#узнать что за тайп
class SingletonMeta(type):
    """
    В Python класс Одиночка можно реализовать по-разному. Возможные способы
    включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
    метаклассом, поскольку он лучше всего подходит для этой цели.
    """

    _instances = {}

    #todo прочитать про эти переменные
    def __call__(cls, *args, **kwargs):
        """
         Данная реализация не учитывает возможное изменение передаваемых
        аргументов в `__init__`.
        :param args:
        :param kwargs:
        :return:
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Наконец, любой одиночка должен содержать некоторую бизнес-логику,
        которая может быть выполнена на его экземпляре.
        """

        #...

if __name__ == '__main__':
    #client code

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("same instance")
    else:
        print("not same instance")

    print("s1 id : {}".format(id(s1)))
    print("s2 id : {}".format(id(s2)))