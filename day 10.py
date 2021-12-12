with open("day 10.txt") as file:
    data = []
    line = file.readline()

    points_dict = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    legal_pair = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    while line:
        new_list = [x for x in line.strip("\n")]
        data.append(new_list)
        line = file.readline()

    # Puzzle 1

    left_side = ["(", "[", "{", "<"]
    corrupted_list = []
    for line in data:
        chuck_list = []
        corrupted = []
        while len(corrupted) == 0:
            for character in line:
                if character in left_side:
                    chuck_list.append(character)
                elif character not in left_side:
                    if character == legal_pair[chuck_list[-1]]:
                        chuck_list = chuck_list[:-1]
                    else:
                        corrupted.append(character)
                        corrupted_list.append(corrupted[0])
                        break
            if len(corrupted) == 0:
                corrupted.append(1)

    print(corrupted_list)
    score = 0
    for corruption in corrupted_list:
        score += points_dict[corruption]
    print(score)

    # Puzzle 2
    score_dict = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    def get_score(list):
        total_score = 0
        for character in list:
            total_score *= 5
            total_score += score_dict[character]
        return total_score
    scores = []
    for line in data:
        chuck_list = []
        added_elements = []
        corrupted = []
        while len(corrupted) == 0:
            for character in line:
                if character in left_side:
                    chuck_list.append(character)
                elif character not in left_side:
                    if character == legal_pair[chuck_list[-1]]:
                        chuck_list = chuck_list[:-1]
                    else:
                        corrupted.append(character)
                        corrupted_list.append(corrupted[0])
                        break
            if len(corrupted) == 0:
                chuck_list.reverse()
                for missing in chuck_list:
                    added_elements.append(legal_pair[missing])
                corrupted.append(1)
        scores.append(get_score(added_elements))
    print(scores)
    score_list = new_list = [x for x in scores if x != 0]
    score_list.sort()
    middle_index = int((len(score_list) - 1)/2)
    print(score_list[middle_index])

