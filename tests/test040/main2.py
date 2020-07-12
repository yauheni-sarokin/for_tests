class CountedObject:
    num_instances = 0

    def __init__(self) -> None:
        self.__class__.num_instances += 1

if __name__ == '__main__':
    counted_object = CountedObject()
    print(counted_object.num_instances)

