# colections


import collections

d = collections.OrderedDict(one=1, two=2, three=3)

if __name__ == '__main__':
    print(d)

    d['four'] = 4

    print(d)

    d.keys()