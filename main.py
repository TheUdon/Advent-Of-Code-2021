with open("day 9.txt") as file:
    # Puzzle 1
    # content = file.read().splitlines()
    # content = [i.split() for i in content]
    # low_points = []
    # row_number = 0
    # for row in content:
    #     new_list = list(row[0])
    #     index = 0
    #     for number in new_list:
    #         if row_number == 0 or row_number == 99:
    #             if row_number == 0:
    #                 up = 9
    #                 below_row = list(content[row_number + 1])
    #                 down = int(below_row[0][index])
    #                 if index == 0:
    #                     left = 9
    #                     right = int(new_list[index + 1])
    #                     if int(new_list[index]) < left and int(new_list[index]) < right and int(new_list[index]) < down and int(new_list[index]) < up:
    #                         low_points.append(int(new_list[index]) + 1)
    #                         index += 1
    #                     else:
    #                         index += 1
    #                 elif index == 99:
    #                     right = 9
    #                     left = int(new_list[index - 1])
    #                     if int(new_list[index]) < left and int(new_list[index]) < right and int(new_list[index]) < down and int(new_list[index]) < up:
    #                         low_points.append(int(new_list[index]) + 1)
    #                         index += 1
    #                     else:
    #                         index += 1
    #                 else:
    #                     left = int(new_list[index - 1])
    #                     right = int(new_list[index + 1])
    #                     if int(new_list[index]) < left and int(new_list[index]) < right and int(new_list[index]) < down and int(new_list[index]) < up:
    #                         low_points.append(int(new_list[index]) + 1)
    #                         index += 1
    #                     else:
    #                         index += 1
    #
    #             elif row_number == 99:
    #                 down = 9
    #                 above_row = list(content[row_number-1][0])
    #                 up = int(above_row[index])
    #                 if index == 0:
    #                     left = 9
    #                     right = int(new_list[index + 1])
    #                     if int(new_list[index]) < left and int(new_list[index]) < right and int(
    #                             new_list[index]) < down and int(new_list[index]) < up:
    #                         low_points.append(int(new_list[index]) + 1)
    #                         index += 1
    #                     else:
    #                         index += 1
    #                 elif index == 99:
    #                     right = 9
    #                     left = int(new_list[index - 1])
    #                     if int(new_list[index]) < left and int(new_list[index]) < right and int(
    #                             new_list[index]) < down and int(new_list[index]) < up:
    #                         low_points.append(int(new_list[index]) + 1)
    #                         index += 1
    #                     else:
    #                         index += 1
    #                 else:
    #                     left = int(new_list[index - 1])
    #                     right = int(new_list[index + 1])
    #                     if int(new_list[index]) < left and int(new_list[index]) < right and int(
    #                             new_list[index]) < down and int(new_list[index]) < up:
    #                         low_points.append(int(new_list[index]) + 1)
    #                         index += 1
    #                     else:
    #                         index += 1
    #
    #         else:
    #             above_row = list(content[row_number - 1][0])
    #             up = int(above_row[index])
    #             below_row = list(content[row_number + 1][0])
    #             down = int(below_row[index])
    #             if index == 0:
    #                 left = 9
    #                 right = int(new_list[index + 1])
    #                 if int(new_list[index]) < left and int(new_list[index]) < right and int(
    #                         new_list[index]) < down and int(new_list[index]) < up:
    #                     low_points.append(int(new_list[index]) + 1)
    #                     index += 1
    #                 else:
    #                     index += 1
    #             elif index == 99:
    #                 right = 9
    #                 left = int(new_list[index - 1])
    #                 if int(new_list[index]) < left and int(new_list[index]) < right and int(
    #                         new_list[index]) < down and int(new_list[index]) < up:
    #                     low_points.append(int(new_list[index]) + 1)
    #                     index += 1
    #                 else:
    #                     index += 1
    #             else:
    #                 left = int(new_list[index - 1])
    #                 right = int(new_list[index + 1])
    #                 if int(new_list[index]) < left and int(new_list[index]) < right and int(
    #                         new_list[index]) < down and int(new_list[index]) < up:
    #                     low_points.append(int(new_list[index]) + 1)
    #                     index += 1
    #                 else:
    #                     index += 1
    #     row_number += 1
    # print(sum(low_points))

    # Puzzle 2
    # Needed to find a different way to set up the data
    # Learned that the concept for this puzzle is 'Flood Fill'(Like the bucket tool in MS Paint)
    data = []
    line = file.readline()
    while line:
        new_list = [x for x in line.strip('\n')]
        int_line = [int(x) for x in new_list]
        data.append(int_line)
        line = file.readline()
    print(data)

    def get_value(data, position):
        # position[0] should be the x coord and position[1] should be the y coord
        if (position[0] < 0) or (position[0] >= len(data)):
            return 10
        if (position[1] < 0) or (position[1] >= len(data)):
            return 10
        return data[position[0]][position[1]]

    basin_list = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            count = 0
            open = [[x, y]]
            closed = []
            while len(open) > 0:
                if (open[0] not in closed) and get_value(data, open[0]) < 9:
                    count += 1
                    closed.append(open[0])
                    xx = open[0][0]
                    yy = open[0][1]
                    offsets = [[xx+1, yy], [xx-1, yy], [xx, yy+1], [xx, yy-1]]
                    for element in offsets:
                        open.append(element)
                del(open[0])
            for element in closed:
                data[element[0]][element[1]] = 9
            if count > 0:
                basin_list.append(count)
    basin_list.sort()
    answer = basin_list[-1] * basin_list[-2] * basin_list[-3]
    print(answer)