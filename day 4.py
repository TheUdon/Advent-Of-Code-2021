# Setting up
with open("day 4.txt") as file:
    bingo_numbers = list(map(int, next(file).split(",")))
    board_number = 0
    boards = []
    for row in file:
        row = row.strip()
        if row == "":
            board = []
            boards.append(board)
            continue
        board += map(int, row.split())
    print(bingo_numbers)

    overall_dict = {"0": []}

    def make_dictionaries():
        for board in boards:
            board_dict = {"A": [], "B": [], "C": [], "D": [], "E": []}
            rows = ["A", "B", "C", "D", "E"]
            letter = 0
            column = 0
            for number in board:
                board_dict[rows[letter]].append(number)
                column += 1
                if column == 5:
                    letter += 1
                    column = 0
            overall_dict["0"].append(board_dict)
        return overall_dict

    def check_row(dictionary):
        for row in dictionary:
            checks = 0
            for number in dictionary[row]:
                if number == -1:
                    checks += 1
                    if checks == 5:
                        return "good"

    def check_column(dictionary):
        rows = ["A", "B", "C", "D", "E"]
        columns = [0, 1, 2, 3, 4]

        for column in columns:
            checks = 0
            for row in rows:
                if dictionary[row][column] == -1:
                    checks += 1
                    if checks == 5:
                        return "good"

    def check_for_winners(dictionary):
        if dictionary["A"][0] == -1 and dictionary["B"][1] == -1 and dictionary["C"][2] == -1 and dictionary["D"][3] == -1 and \
                dictionary["E"][4] == -1:
            return "winner"
        elif dictionary["E"][0] == -1 and dictionary["D"][1] == -1 and dictionary["C"][2] == -1 and dictionary["D"][3] == -1 and \
                dictionary["A"][4] == -1:
            return "winner"
        elif check_row(dictionary) == "good":
            return "winner"
        elif check_column(dictionary) == "good":
            return "winner"
        else:
            pass

    def calc_score(dictionary, winning_number):
        sum = 0
        for row in dictionary:
            for number in dictionary[row]:
                if number != -1:
                    sum += number
        total_score = winning_number * sum
        return total_score


    make_dictionaries()

    # Puzzle 1

    # index = 0
    # winner = False
    # while not winner:
    #     print(index)
    #     for a_dict in overall_dict["0"]:
    #         for row in a_dict:
    #             a_dict[row] = [-1 if bingo_numbers[index] == a_dict[row][i] else a_dict[row][i] for i in range(len(a_dict[row]))]
    #             if check_for_winners(a_dict) == "winner":
    #                 print(a_dict)
    #                 print(calc_score(a_dict, bingo_numbers[index]))
    #                 winner = True
    #     index += 1

    # Puzzle 2
    index = 0
    winner = False
    while winner:
        for a_dict in overall_dict["0"]:
            winner_list = []
            for row in a_dict:
                a_dict[row] = [-1 if bingo_numbers[index] == a_dict[row][i] else a_dict[row][i] for i in
                               range(len(a_dict[row]))]
            if check_for_winners(a_dict) == "winner":
                winner_list.append(a_dict)
                print(len(overall_dict["0"]))
                if len(overall_dict["0"]) == 1:
                    winner = True

            for winner in winner_list:
                if winner in overall_dict["0"]:
                    overall_dict["0"].remove(winner)
                    print(len(overall_dict["0"]))
        index += 1









