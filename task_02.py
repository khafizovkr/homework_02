some_list = []
n = int(input('Сколько элементов будет в списке? '))
for i in range(n):
    i = input(f'Введите {i + 1}-й элемент списка: ')
    some_list.append(i)
print(some_list)

for i in range(0, n, 2):
    if i < (n/2):
        some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
print(some_list)