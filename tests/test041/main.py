from datetime import date


class Person:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 birth_date: date, job, working_years, salary, country, city, gender='uknown'):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__job = job
        self.__working_years = working_years
        self.__salary = salary
        self.__country = country
        self.__city = city
        self.__gender = gender

    # проперти должны возвращать только одно значение, это геттер
    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def birth_date(self):
        return self.__birth_date

    # Возвращает не свойство а какую либо дополнительную более сложную информацию
    def get_name(self):
        return f'{self.__first_name} {self.__last_name}'

    def get_age(self):
        timedelta = date.today() - self.__birth_date
        years = timedelta.days // 365
        return years


if __name__ == '__main__':
    # обьекты к маленькой буквы
    person = Person('James', 'Holt', date(2000, 1, 1), 'surgeon', '10', '5000', 'Germany', 'Berlin', 'male')

    # Выводим в консоль свойства
    print(person.first_name)
    print(person.birth_date)

    # Выводим в консоль имя, возраст
    print(person.get_name())
    print(person.get_age())
