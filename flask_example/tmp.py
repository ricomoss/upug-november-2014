

def fib(n):
    if n < 2:
        return 0
    a = 0
    b = 1
    i = 0
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
    return b


if __name__ == '__main__':
    print fib(4)