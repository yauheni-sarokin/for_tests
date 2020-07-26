# Merge dictionaries


xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

if __name__ == '__main__':
    zs = {**xs, **ys}
    print(zs)
    zs2 = {**xs}
    print(zs2)