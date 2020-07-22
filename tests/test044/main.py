# Loping & Iteration ...
# Comrehending comprehensions


# values = [expression for item in collection]
squares = [x * x for x in range(10)]

# equal to
# values = []
# for item in collection:
# values.append(expression)

even_squares = [x * x for x in range(10) if x % 2 == 0]

# equal to
# values = [expression
# for item in collection
# if condition]

# dict and sets

dict_even_squares = {x: x * x for x in range(10) if x % 2 == 0}

if __name__ == '__main__':
    print(squares)
    print(even_squares)
    print(dict_even_squares)