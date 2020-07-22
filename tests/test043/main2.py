from struct import Struct

MyStruct = Struct('i?f')

data = MyStruct.pack(23, False, 42.0)

if __name__ == '__main__':
    print(f'{data}')

    print(MyStruct.unpack(data))