def square(a):
    return a * a


def my_pow(n, p):
    r = n
    for i in range(1, p):
        r = r * n
    return r

