my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите число: '))
print(my_list)
for i in range(len(my_list)):
    if new_el >= my_list[i]:
        my_list.insert(i, new_el)
        break
    elif new_el < my_list[-1]:
        my_list.append(new_el)
        break
print(my_list)
