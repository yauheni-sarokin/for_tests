# lambdas

if __name__ == '__main__':
    add = lambda x, y: x + y
    print(add(5, 3))

    # or...

    print((lambda x, y: x + y)(3, 5))

    tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
    print(sorted(tuples, key=lambda x: x[1]))
    print(sorted((range(-3, 6)), key=lambda x: x * x))

    print(range(-5, 6))

    key = lambda x: x * x
    print(key(2))
