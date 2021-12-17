import collections
with open("day 14.txt") as file:
    # Puzzle 1
    content = file.read().splitlines()
    poly_temp = content[0]
    file.readline()

    pair_content = content[2:]
    pair_dict = {}
    for pair in pair_content:
        split = pair.split(" -> ")
        pair_dict[split[0]] = split[1]
    print(poly_temp)

    for step in range(10):
        new_string = poly_temp[0]
        for x in range(len(poly_temp) - 1):
            string = poly_temp[x] + poly_temp[x + 1]
            new_string += pair_dict[string] + poly_temp[x + 1]
        poly_temp = new_string

    elements = set(poly_temp)
    count_dict = {char: poly_temp.count(char) for char in elements}
    print(count_dict)
    highest = 0
    lowest = 100000000000000000
    for key in count_dict:
        if count_dict[key] > highest:
            highest = count_dict[key]
        if count_dict[key] < lowest:
            lowest = count_dict[key]
    ans = highest - lowest
    print(ans)

    # Puzzle 2
    poly_temp = content[0]
    pair_count = collections.Counter()

    for x in range(len(poly_temp) - 1):
        pair_count[poly_temp[x:x + 2]] += 1

    for step in range(40):
        new_count = collections.Counter()
        char_count = collections.Counter()
        for pair, count in pair_count.items():
            new_count[f"{pair[0]}{pair_dict[pair]}"] += count
            new_count[f"{pair_dict[pair]}{pair[1]}"] += count

            char_count[pair[0]] += count
            char_count[pair_dict[pair]] += count
        pair_count = new_count
    char_count[poly_temp[-1]] += 1

    sorted_list = sorted(char_count.values())

    highest = sorted_list[-1]
    lowest = sorted_list[0]
    ans = highest - lowest
    print(ans)