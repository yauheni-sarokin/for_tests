# Generators


def repeater(value):
    while True:
        yield value

def repeat_three_times(value):
    yield value
    yield value
    yield value

if __name__ == '__main__':
    # for x in repeater('Hi'):
    #     print(x)
    obj = repeater('hey')
    print(obj.__next__())
    print(next(obj))

    for x in repeat_three_times('hou'):
        print(x)