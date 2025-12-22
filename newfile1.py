from itertools import takewhile

def numbers():
    for i in range(1, 10):
        yield i

print(list(takewhile (lambda x: x % 2 != 0, numbers())))