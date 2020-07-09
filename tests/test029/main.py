# with open('helo.txt', 'w') as f:
#     f.write('hello, world!')

#
# some_lock = threading.Lock()
# # Harmful:
# some_lock.acquire()
# try:
# # Do something...
# finally:
# some_lock.release()
# # Better:
# with some_lock:
# # Do something...

# support own with

class ManagedFile:

    def __init__(self, name):
        self.name = name


    def __enter__(self):
        self.file = open(self.name, 'w')

        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

if __name__ == '__main__':
    with ManagedFile('hello.txt') as f:
        f.write('hellooooo')
        f.write('byyyyye')