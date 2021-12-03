# Setting up
with open("day 2.txt") as directions:
    starting_list = directions.read()
    element_list = []
    for element in starting_list:
        element_list.append(element)
    directions_list = []
    current_element = 0
    action = ""
    for element in element_list:
        if element != "\n":
            action += element
            current_element += 1
            if current_element == 7783:
                # len(element_list) outputs 7783
                directions_list.append(action)
        elif element == "\n":
            directions_list.append(action)
            current_element += 1
            action = ""
    directions_dict = {
        "forward": [],
        "up": [],
        "down": []
    }

    for direction in directions_list:
        array = direction.split()
        if array[0] == "forward":
            directions_dict["forward"].append(int(array[1]))
        elif array[0] == "up":
            directions_dict["up"].append(int(array[1]))
        elif array[0] == "down":
            directions_dict["down"].append(int(array[1]))

    # Part 1

    horizontal_position = sum(directions_dict["forward"])
    up_sum = sum(directions_dict["up"])
    down_sum = sum(directions_dict["down"])

    depth = down_sum - up_sum

    multiplication = depth * horizontal_position
    # print(multiplication)
    # the answer is 1693300

    # Part 2

    aim = 0
    horizontal_position = 0
    depth = 0

    for direction in directions_list:
        array = direction.split()
        if array[0] == "forward":
            horizontal_position += int(array[1])
            depth += (int(array[1]) * aim)
        elif array[0] == "up":
            aim -= int(array[1])
        elif array[0] == "down":
            aim += int(array[1])
    answer = horizontal_position * depth
    # print(answer)
    # the answer is 1857958050

