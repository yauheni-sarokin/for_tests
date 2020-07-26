# pretty printing
import json

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}

if __name__ == '__main__':
    x = json.dumps(mapping, indent=10, sort_keys=True)
    print(x)
