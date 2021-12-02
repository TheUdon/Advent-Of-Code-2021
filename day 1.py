with open("puzzle 1.txt") as numbers:
    number_list = numbers.read()
    list_2 = []
    for number in number_list:
        list_2.append(number)
    list_3 = []
    current_element = 0
    number_for_list = ""
    for element in list_2:
        if element != "\n":
            number_for_list += element
            current_element += 1
            if current_element == 9832:
                list_3.append(int(number_for_list))
        elif element == "\n":
            list_3.append(int(number_for_list))
            current_element += 1
            number_for_list = ""
        elif current_element == 9831:
            list_3.append(int(number_for_list))

    # Puzzle 1
    # increases = 0
    # for number in range(0, len(list_3)):
    #     if list_3[number] > list_3[number-1]:
    #         increases += 1
    #     elif list_3[number] == 0:
    #         pass
    #
    # print(len(list_3))
    # print(increases)

    # Puzzle 2
    list_4 = []
    for num in range(0, len(list_3)-2):
        sum_of_nums = list_3[num] + list_3[num + 1] + list_3[num + 2]
        list_4.append(sum_of_nums)
    print(list_4)

    increases = 0
    for number in range(0, len(list_4)):
        if list_4[number] > list_4[number-1]:
            increases += 1
        elif list_4[number] == 0:
            pass

    print(len(list_4))
    print(increases)