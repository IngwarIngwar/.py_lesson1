check_int = 9
check_float = 5.6
check_str = "Какой-то текст"
check_list = ['ж', '6']
check_tuple = ('ж', '8')
check_dict = {'Фрукт': 'Яблоко', 'Имя': 'Иван'}
super_list = [check_int, check_float, check_str, check_list, check_tuple, check_dict]
for i in super_list:
    print(f'{i} это {type(i)}')