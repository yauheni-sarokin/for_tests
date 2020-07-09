from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


if __name__ == '__main__':
    with managed_file("hyyyee.txt") as f:
        f.write('hie bye')
