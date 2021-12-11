from collections import Counter
# Setting up
with open("day 6.txt") as file:
    fish_times = list(map(int, next(file).split(",")))
    # Puzzle 1
    # for day in range(80):
    #     fish_times.extend([9] * fish_times.count(0))
    #     fish_times = list(map(lambda fish: fish + 6 if fish == 0 else fish - 1, fish_times))
    # print(len(fish_times))

    # Puzzle 2
    # First time using the collections module, had to look up a faster way to do a loop like this
    fish_dict = Counter(fish_times)
    print(fish_dict)

    for day in range(256):
        zeroes = fish_dict[0]
        fish_dict[0] = fish_dict[1]
        fish_dict[1] = fish_dict[2]
        fish_dict[2] = fish_dict[3]
        fish_dict[3] = fish_dict[4]
        fish_dict[4] = fish_dict[5]
        fish_dict[5] = fish_dict[6]
        fish_dict[6] = fish_dict[7]
        fish_dict[6] += (zeroes)
        fish_dict[7] = fish_dict[8]
        fish_dict[8] = zeroes
        print(day)

    print(sum(x for x in fish_dict.values()))