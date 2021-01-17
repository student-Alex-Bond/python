with open("text.txt", "w") as f_obj:
    while True:
        my_str = input("Введите что - нибудь: ")
        if len(my_str) > 0:
            f_obj.writelines(my_str + "\n")
        else:
            break
