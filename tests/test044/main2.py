# list slicing tricks and sushi operator


lst = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    # lst[start:end:step]
    print(lst[1:3:1])
    # stride - every second parameter
    print(lst[::2])
    # sushi operator - reversion
    print(lst[::-1])
    #del all
    del lst[:]
    print(lst)
