import sys
result = 0
while True:
    line = input("Введите строку чисел, разделенных пробелом. Для выходна введите Q: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'q':
                print(f"Ваша сумма равна {result}. Программа завершена")
                exit(0)
            else:
                print(f"Ваша сумма равна {result}. Некорректный ввод", file=sys.stderr)
                exit(1)