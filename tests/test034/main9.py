def logger(func):
    print(f'before executing command ')
    return func


@logger
def summer(x: int, y: int) -> int:
    return x + y

@logger
def differ(x: int, y: int) -> int:
    return x - y


if __name__ == '__main__':
    summ = differ(1, 2)
    print(summ)
