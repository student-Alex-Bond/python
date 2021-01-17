import json


with open("text7.txt", 'r') as f:
    my_list = list()
    my_dict = dict()
    average_profit = list()
    list_profit = list()
    firms_with_losses = list()
    for el in f.read().split('\n'):
        my_str = el.split()
        for i in my_str:
            if i.isdigit():
                list_profit.append(i)
        profit = int(list_profit[0]) - int(list_profit[1])
        if profit > 0:
            my_list.append(my_str[0])
            my_list.append(profit)
            average_profit.append(profit)
        else:
            firms_with_losses.append(my_str[0])
            firms_with_losses.append(profit)
        aver_summa = 0
        for i in average_profit:
            aver_summa = aver_summa + int(i)
        aver_profit = aver_summa / len(average_profit)
        list_profit.clear()
        list_aver_profit = ['average profit']
        list_aver_profit.append(aver_profit)
av_profit = dict([list_aver_profit])
profit_making_firms = dict({my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)})
firm_with_losses = dict({firms_with_losses[i]: firms_with_losses[i + 1] for i in range(0, len(firms_with_losses), 2)})
final_list = [{**av_profit}, 'firms_with_losses', {**firm_with_losses}, 'profit_making_firms', {**profit_making_firms}]
print(final_list)
with open("final_list.json", "w") as write_f:
    json.dump(final_list, write_f)

with open("final_list.json") as read_f:
    data = json.load(read_f)

print(data)
