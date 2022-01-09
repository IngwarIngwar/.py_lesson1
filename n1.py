data_list = [7, 20.4,'red', (20, 30, True), {'name' : 'Roy', 'address' : 'home'}]

for i, item in enumerate (data_list, 1):
    print(f"{i}){item} - {type(item)}")