# Setting up
with open("day 8.txt") as file:

    digit_length_list = [2, 4, 3, 7]
    # the lengths for 1, 4, 7. and 8 respectively

    content = file.read().splitlines()
    content = [i.split() for i in content]
    data_list = []
    for number in content:
        data = []
        for element in number:
            if element == "|":
                pass
            else:
                data.append(element)
        data_list.append(data)

    # Puzzle 1
    appearances = 0
    for input in data_list:
        for led in input[10:14]:
            if len(led) in digit_length_list:
                appearances += 1
    print(appearances)

    # Puzzle 2
    outputs = []
    for input in data_list:
        number_dict = {}
        for number in input[0:10]:
            if len(number) == 2:
                number_dict[1] = number
            elif len(number) == 4:
                number_dict[4] = number
            elif len(number) == 3:
                number_dict[7] = number
            elif len(number) == 7:
                number_dict[8] = number

        for number in input[0:10]:
            if len(number) == 6:
                check = list(number_dict[4])
                character_list = list(number)
                for character in check:
                    if character in character_list:
                        character_list.remove(character)

                if len(character_list) == 2:
                    number_dict[9] = number

                elif len(character_list) == 3:
                    check = list(number_dict[1])
                    character_list = list(number)
                    for character in check:
                        if character in character_list:
                            character_list.remove(character)

                    if len(character_list) == 5:
                        number_dict[6] = number
                    elif len(character_list) == 4:
                        number_dict[0] = number

            elif len(number) == 5:
                check = list(number_dict[1])
                character_list = list(number)
                for character in check:
                    if character in character_list:
                        character_list.remove(character)

                if len(character_list) == 3:
                    number_dict[3] = number

                elif len(character_list) == 4:
                    check = list(number_dict[4])
                    character_list = list(number)
                    for character in check:
                        if character in character_list:
                            character_list.remove(character)
                    if len(character_list) == 3:
                        number_dict[2] = number
                    elif len(character_list) == 2:
                        number_dict[5] = number
        print(input[10:14])
        print(number_dict)
        output = ""
        for led in input[10:14]:
            print(led)
            if len(led) == 2:
                output += str(1)
            elif len(led) == 4:
                output += str(4)
            elif len(led) == 3:
                output += str(7)
            elif len(led) == 7:
                output += str(8)
            elif len(led) == 5 or len(led) == 6:
                for key in number_dict:
                    character_list = list(led)
                    dictionary_list = list(number_dict[key])
                    if len(led) == len(dictionary_list):
                        for character in character_list:
                            if character in dictionary_list:
                                dictionary_list.remove(character)
                        if len(dictionary_list) == 0:
                            output += str(key)
            print(output)
        outputs.append(int(output))

    print(sum(outputs))