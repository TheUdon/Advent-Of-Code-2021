# Setting up
with open("day 7.txt") as file:
    content = list(map(int, next(file).split(",")))
    min_position = min(content)
    max_position = max(content)
    print(content)
    print(min_position)
    print(max_position)
    # lowest horizontal position is 0 and the highest horizontal position is 1892

    # Puzzle 1
    # fuel_list = []
    # for x in range(min_position, max_position + 1):
    #     fuel_use = []
    #     for crab in content:
    #         fuel = crab - x
    #         fuel_use.append(abs(fuel))
    #     total_fuel = sum(fuel_use)
    #     fuel_list.append(total_fuel)
    # print(fuel_list)
    # print(min(fuel_list))

    # Puzzle 2
    fuel_list = []
    for x in range(min_position, max_position + 1):
        fuel_use = []
        for crab in content:
            steps = abs(crab - x)
            fuel = sum([step for step in range(1, steps + 1)])
            fuel_use.append(fuel)
        total_fuel = sum(fuel_use)
        fuel_list.append(total_fuel)
    print(fuel_list)
    print(min(fuel_list))