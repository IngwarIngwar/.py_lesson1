#user_month = int(input('Введите номер месяца: '))
#seasons_list = [[1 ,2 ,12, 'зима'], [3, 4, 5, 'весна'], [6, 7, 8, 'лето'], [9, 10, 11, 'осень']]
#for el in seasons_list:
 #   if user_month in el:
 #       print(el[3])

month = int(input("Введите номер месяца: "))
if month <= 12 and month >= 1:
    month_dict = {1: 'Январь',
                  2: 'Февраль',
                  3: 'Март',
                  4: 'Апрель',
                  5: 'Май',
                  6: 'Июнь',
                  7: 'Июль',
                  8: 'Август',
                  9: 'Сентябрь',
                  10: 'Октябрь',
                  11: 'Ноябрь',
                  12: 'Декабрь'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == month-1:
            print(f"Ваш месяц (список) - {month_list[i]}")
            break
    print(f"Ваш месяц (словарь) - {month_dict[month]}")