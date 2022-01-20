#def my_func(x, y):
#    return 1 / x ** abs(y)
#print(my_func(2, -3))


def my_func(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

print(my_func(float(input("Первое число - ")), int(input("Второе число - "))))