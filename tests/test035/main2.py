# function argument unpacking


def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


if __name__ == '__main__':
    print_vector(0, 1, 0)

    tuple_vec = (1, 0, 1)
    list_vec = [1, 0, 1]

    print_vector(*tuple_vec)
    print_vector(*list_vec)

    gen_expr = (x * x for x in range(3))
    print_vector(*gen_expr)

    dict_vec = {'y': 0, 'z': 1, 'x': 1}
    print_vector(**dict_vec)
