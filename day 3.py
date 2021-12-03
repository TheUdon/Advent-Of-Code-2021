# Setting up
with open("day 3.txt") as content:
    starting_list = content.read()
    element_list = []
    for element in starting_list:
        element_list.append(element)
    binary_dict = {}
    current_element = 0
    position_in_bit = 0
    for element in element_list:
        if element != "\n":
            if str(position_in_bit) not in binary_dict.keys():
                binary_dict[str(position_in_bit)] = [element]
                position_in_bit += 1
                current_element += 1
            else:
                binary_dict[str(position_in_bit)].append(element)
                position_in_bit += 1
                current_element += 1

        elif element == "\n":
            current_element += 1
            position_in_bit = 0
    # print(binary_dict)

    # Part 1
    # for bit in binary_list:
    gamma_rate_binary = ""
    epsilon_rate_binary = ""
    for position in binary_dict:
        list = binary_dict[position]
        most_common = max(list, key=list.count)
        least_common = min(list, key=list.count)
        gamma_rate_binary += most_common
        epsilon_rate_binary += least_common
    # print(gamma_rate_binary)
    # outputs 000011011001
    # print(epsilon_rate_binary)
    # outputs 111100100110

    # finding the values from the binary

    gamma_rate = int(gamma_rate_binary, 2)
    epsilon_rate = int(epsilon_rate_binary, 2)
    # print(gamma_rate)
    # gamma_rate is 217
    # print(epsilon_rate)
    # epsilon_rate is 3878

    power_consumption = gamma_rate * epsilon_rate
    # print(power_consumption)
    # the answer is 841526

    # Part 2
    oxygen_list = []
    CO2_list = []
    current_element = 0
    binary = ""
    for element in element_list:
        if element != "\n":
            binary += element
            current_element += 1
            if current_element == len(element_list):
                oxygen_list.append(binary)
                CO2_list.append(binary)
        elif element == "\n":
            oxygen_list.append(binary)
            CO2_list.append(binary)
            current_element += 1
            binary = ""


    def get_list(str):
        return [char for char in str]

    def reduce_list(list, remove_list):
        for remove in remove_list:
            list.remove(remove)

    def find_oxygen_binary(input_dict, position):
        char_list = input_dict[str(position)]
        one = char_list.count("1")
        zero = char_list.count("0")
        if one == zero:
            most_common_value = 1
        elif one > zero:
            most_common_value = 1
        else:
            most_common_value = 0
        need_to_remove = []
        for number in oxygen_list:
            list = get_list(number)
            if list[int(position)] != str(most_common_value):
                need_to_remove.append(number)

        reduce_list(oxygen_list, need_to_remove)
        return oxygen_list


    def find_CO2_binary(input_dict, position):
        char_list = input_dict[str(position)]
        one = char_list.count("1")
        zero = char_list.count("0")
        if one == zero:
            least_common_value = 0
        elif one > zero:
            least_common_value = 0
        else:
            least_common_value = 1
        need_to_remove = []
        for number in CO2_list:
            list = get_list(number)
            if list[int(position)] != str(least_common_value):
                need_to_remove.append(number)

        reduce_list(CO2_list, need_to_remove)
        return CO2_list

    def make_dictionary(list):
        new_dict ={}
        position_in_bit = 0
        for number in list:
            char_list = get_list(number)
            for element in char_list:
                if str(position_in_bit) not in new_dict.keys():
                    new_dict[str(position_in_bit)] = [element]
                    position_in_bit += 1
                else:
                    new_dict[str(position_in_bit)].append(element)
                    position_in_bit += 1
            position_in_bit = 0
        return new_dict

    position_in_dict = 0
    oxygen_binary = ""
    CO2_binary = ""

    run = True
    while run:
        oxygen_dict = make_dictionary(oxygen_list)
        CO2_dict = make_dictionary(CO2_list)
        if len(oxygen_list) != 1:
            oxygen_binary = find_oxygen_binary(oxygen_dict, position_in_dict)[0]
        if len(CO2_list) != 1:
            CO2_binary = find_CO2_binary(CO2_dict, position_in_dict)[0]
        position_in_dict += 1
        if len(oxygen_list) == 1 and len(CO2_list) == 1:
            run = False
    # print(oxygen_binary)
    # output is 010010011001
    # print(CO2_binary)
    # output is 111111100110


    oxygen_generator_rating = int(oxygen_binary, 2)
    CO2_scrubber_rating = int(CO2_binary, 2)
    # print(oxygen_generator_rating)
    # output is 1177
    # print(CO2_scrubber_rating)
    # output is 4070


    life_support_rating = oxygen_generator_rating * CO2_scrubber_rating
    print(life_support_rating)
    # Answer is 4790390