while True:
    days = 1
    start_km = float(input('Введите начальный результат - '))
    target_km = float(input('Введите конечный результат - '))
    while start_km < target_km:
        start_km = start_km * 1.1
        days = days + 1
        print(days) #результат выводит в столбик, как сделать, чтобы только ответ выводил?
