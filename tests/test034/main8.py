import functools


# decorating functions that accept arguments

def trace(func):
    """
    Trace decorator wraps function
    :param func: any function
    :return: return wrapper original function
    """

    @functools.wraps(func)  # to use doc from wrapped function
    def wrapper(*args, **kwargs):
        """
        Trace wrapper
        :param args:
        :param kwargs:
        :return:
        """
        print(f'TRACE: calling {func.__name__}()'
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result

    return wrapper


@trace
def say(name, line):
    """
    name says something
    :param name:
    :param line:
    :return:
    """
    return f'{name}: {line}'


if __name__ == '__main__':
    print(say('Jane', 'Hello, World'))
    print(say.__doc__)
