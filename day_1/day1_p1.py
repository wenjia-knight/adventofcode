with open('input.txt') as input:
    lines = input.readlines()

for line in lines:
    calories = [line.strip() for line in lines]

total_sum = []
each_sum = 0
for calorie in calories:
    if calorie != "":
        each_sum += int(calorie)
    else:
        total_sum.append(each_sum)
        each_sum = 0
print(max(total_sum))