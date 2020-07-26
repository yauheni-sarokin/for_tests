# switch/case with dicts


x = {True: 'yes', 1: 'no', 10: 'maybe'}
y = {1: 'no', 1.0: 'maybe'}

if __name__ == '__main__':
    print(x)
    print(y)
    print(int('1') == True)