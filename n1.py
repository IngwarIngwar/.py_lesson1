def division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    except ValueError:
        return "Ввод только для чисел"
print(division(int(input("Введите первое число: ")), int(input("Введите второе число: "))))