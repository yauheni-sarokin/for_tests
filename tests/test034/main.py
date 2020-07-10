# Functions are firs class objects


def yell(text):
    return text.upper() + '!'


if __name__ == '__main__':
    bark = yell
    print(bark('woof'))
