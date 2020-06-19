class Property:

    def __init__(self) -> None:
        self._my_value = None

    @property
    def my_value(self) -> int:
        return self._my_value
    
    @my_value.setter
    def my_value(self, my_value: int) -> None:
        self._my_value = my_value
        
if __name__ == '__main__':
    _property = Property()
    _property.my_value = 2

    print(_property.my_value)

