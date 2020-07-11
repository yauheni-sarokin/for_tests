# modified behaviour by decorator


def uppercase(func):
    def wrapper():
        original_result: str = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper

@uppercase
def get_hello():
    return 'hello'

if __name__ == '__main__':
    print(get_hello())