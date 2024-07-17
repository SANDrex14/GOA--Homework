list0 = []

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

list0.append(list1)
list0.append(list2)


for inner_list in list0:
    for item in inner_list:
        print(item)