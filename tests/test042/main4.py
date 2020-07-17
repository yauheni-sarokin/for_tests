# array

import array

arr = array.array('f', [1., 2., 3.])
bytes_array = bytes((1, 2, 3, 4, 10))

if __name__ == '__main__':
    print(arr)
    arr.append(1)
    print(arr)

    print(bytes_array)