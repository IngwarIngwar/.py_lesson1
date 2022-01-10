user_month = int(input('Введите номер месяца: '))
seasons_list = [[1 ,2 ,12, 'зима'], [3, 4, 5, 'весна'], [6, 7, 8, 'лето'], [9, 10, 11, 'осень']]
for el in seasons_list:
    if user_month in el:
        print(el[3])