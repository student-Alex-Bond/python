my_list = [7, 5, 3, 3, 3, 2]
my_list1 = my_list.copy()
rating = int(input('Введите новый элемент рейтинга: '))
maxi = max(my_list1)
x = my_list1.index(maxi)
mini = min(my_list1)
z = my_list1.index(mini)
if rating > maxi:
    my_list1.insert(x,rating)
if rating < mini:
    my_list1.insert(z+1,rating)
for el in my_list1:
    if rating == el:
        k = my_list1.index(el)
        my_list1.insert(k, rating)
        break

print(my_list1)
