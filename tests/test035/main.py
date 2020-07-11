# args kwargs


def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


if __name__ == '__main__':
    foo('hi', 1, 2, 3, key1='value', number=123)
