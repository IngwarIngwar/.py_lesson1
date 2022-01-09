a = input('Введите числа, разделяя пробелами: ').split()
i = 0
print(a)
while i + 1 < len(a):
    if i % 2 == 0:
        a.insert(i, a.pop(i+1))
    i += 1
print(a)