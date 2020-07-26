# Bounded repeater


def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value


def bounded_repeater2(value, max_repeats):
    for i in range(max_repeats):
        yield value


for x in bounded_repeater('hi', 4):
    print(x)
