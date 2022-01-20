def my_func(a, b, c):
    sequence = [a, b, c]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))
my_func(-58, 15, 55)