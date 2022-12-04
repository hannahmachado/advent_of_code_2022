with open("solutions/dec_01/input.tsv")as f:
    line = [line.strip('\n') for line in f]
    total_calories = []
    sum = 0
    for calorie in line:
        if len(calorie) != 0:
            sum += int(calorie)
        else:
            total_calories.append(sum)
            sum = 0

    top_3_sum = sum(sorted(total_calories, reverse=True)[0:3])
    print(top_3_sum)
