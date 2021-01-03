from sys import argv

script_name, output_in_hours, rate_per_hour, prize = argv

wage = (float(output_in_hours) * float(rate_per_hour)) + float(prize)

print("Выработка в часах: ", output_in_hours)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", prize)
print("Заработная плата: ", wage)
