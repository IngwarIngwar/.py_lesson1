goods = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'Единица измерения': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'E', для продолжения нажмите 'Enter', для аналитики нажмите 'A': ").upper()
    if control == 'E':
        break
    num += 1
    if control == 'A':
        print(f'\n Аналитика \n{"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>1}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Введите значение "{f}" ')
        features[f] = int(feature_) if (f == 'Цена' or f == 'Количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))