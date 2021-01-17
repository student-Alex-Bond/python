with open("text1.txt", "r") as f:
    count = 0
    for line in f:
        my_list = line.split()
        count += 1
        print(f'Слов в {count}-й строке: {len(my_list)}')
    print(f"Строк в файле: {count}")
