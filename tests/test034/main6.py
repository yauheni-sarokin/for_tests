# decorators


def null_decorator(func):
    print(f'decorated')
    func1 = func('ff')
    print(f'executed {func1}')
    return func


@null_decorator
def greet(name='some'):
    return f'Hello {name}'


if __name__ == '__main__':
    print(greet('yo'))
