with open("text2.txt", 'r') as f, open('text3.txt', 'w') as fil:
    my_dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
    my_str = str()
    for line in f:
        line = line.split()
        for item in my_dict.items():
            if line[0] == item[0]:
                line[0] = item[1]
                my_str = " ".join(line)
                fil.writelines(my_str + '\n')
# with open('text3.txt', 'w') as fil:
#     for el in my_list:
#         my_str = str(el)
#         my_str.split()
#         fil.writelines(my_str)
