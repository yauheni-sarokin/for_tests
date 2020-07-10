class Student():

    def __init__(self, name: str, age: int) -> None:
        print(f'initialize {self.__class__}')
        self.__name = name  # private
        self.age = age  # public

    @property
    def name(self) -> str:
        print(f'getter called')
        return self.__name

    @name.setter
    def name(self, new_name: str):
        # assert throw error if not true : assert condition, message
        assert isinstance(new_name, str), 'NAME IS NOT A STRING!!!'
        print(f'setter called, set name {new_name}')
        self.__name = new_name


if __name__ == '__main__':
    student = Student('John', 20)

    print(student.name)  # old name
    student.name = 'Andrey'
    # student.name = '123'
    print(student.name)  # new name

    #here propgram stops
    import sys
    sys.exit(0)
    student = 123
    # is instance check if object belongs to class
    if isinstance(student, Student):
        print(f'Yes, it is')
    else:
        print(f'No, it is not')

    # del student.age
    # print(student.age)
    # print(student.__name)
    # print(student.name)
    # student.name = 'Jimmy'
