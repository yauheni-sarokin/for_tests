# Dictionary default values
import operator

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

if __name__ == '__main__':
    sort = sorted(xs.items(), key=lambda x: x[1])
    print(sort)

    l = sorted(xs.items(), key=operator.itemgetter(1))
    print(l)