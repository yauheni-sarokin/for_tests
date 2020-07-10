def yell(text: str):
    return text.upper() + '!'


bark = yell


if __name__ == '__main__':
    del yell
    print(bark('hey'))
    print(bark.__name__)
    print(bark.__qualname__)

    funcs = [bark, str.lower, str.capitalize]

    print(funcs)

    for f in funcs:
        print(f, f('hey'))