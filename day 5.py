# Setting up
import json

with open("day 5.txt") as file:
    content = file.read()
    data = content.split('\n')
    data = [x.replace(" -> ", ",") for x in data]
    data = [x.split(",") for x in data]
    print(data)
    coordinate_dict = {
        "x1": [],
        "y1": [],
        "x2": [],
        "y2": [],
    }

    for row in data:
        coordinate_dict["x1"].append(int(row[0]))
        coordinate_dict["y1"].append(int(row[1]))
        coordinate_dict["x2"].append(int(row[2]))
        coordinate_dict["y2"].append(int(row[3]))

    print(json.dumps(coordinate_dict, indent=4))

    max_x1 = max(coordinate_dict["x1"])
    max_y1 = max(coordinate_dict["y1"])
    # max_x2 = max(coordinate_dict["x2"])
    # max_y2 = max(coordinate_dict["y2"])
    # print(max_x1)
    # print(max_y1)
    # print(max_x2)
    # print(max_y2)
    # max x is 990 and max y is 989

    grid = []
    for y in range(max_y1):
        grid.append([])
        for x in range(max_x1):
            grid[y].append(0)

    # Puzzle 1
    # for num in range(len(data)):
    #     x1 = coordinate_dict["x1"][num]
    #     y1 = coordinate_dict["y1"][num]
    #     x2 = coordinate_dict["x2"][num]
    #     y2 = coordinate_dict["y2"][num]
    #     if x1 == x2 or y1 == y2:
    #         if x1 == x2:
    #             if y1 > y2:
    #                 for y_add in range(y2, y1+1):
    #                     grid[y_add-1][x1-1] += 1
    #             elif y2 > y1:
    #                 for y_add in range(y1, y2+1):
    #                     grid[y_add-1][x1-1] += 1
    #         elif y1 == y2:
    #             if x1 > x2:
    #                 for x_add in range(x2, x1+1):
    #                     grid[y1-1][x_add-1] += 1
    #             elif x2 > x1:
    #                 for x_add in range(x1, x2+1):
    #                     grid[y1-1][x_add-1] += 1

    # Puzzle 2
    for num in range(len(data)):
        x1 = coordinate_dict["x1"][num]
        y1 = coordinate_dict["y1"][num]
        x2 = coordinate_dict["x2"][num]
        y2 = coordinate_dict["y2"][num]
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                if y1 > y2:
                    for y_add in range(y2, y1+1):
                        grid[y_add-1][x1-1] += 1
                elif y2 > y1:
                    for y_add in range(y1, y2+1):
                        grid[y_add-1][x1-1] += 1
            elif y1 == y2:
                if x1 > x2:
                    for x_add in range(x2, x1+1):
                        grid[y1-1][x_add-1] += 1
                elif x2 > x1:
                    for x_add in range(x1, x2+1):
                        grid[y1-1][x_add-1] += 1
        else:
            if x1 > x2:
                if y1 > y2:
                    for y_add in range(y2, y1+1):
                        grid[y1-1][x1-1] += 1
                        y1 -= 1
                        x1 -= 1
                elif y2 > y1:
                    for y_add in range(y1, y2+1):
                        grid[y1-1][x1-1] += 1
                        y1 += 1
                        x1 -= 1
            elif x2 > x1:
                if y1 > y2:
                    for y_add in range(y2, y1+1):
                        grid[y1-1][x1-1] += 1
                        y1 -= 1
                        x1 += 1
                elif y2 > y1:
                    for y_add in range(y1, y2+1):
                        grid[y1-1][x1-1] += 1
                        y1 += 1
                        x1 += 1

    overlap = 0
    for row in grid:
        for number in row:
            if number > 1:
                overlap += 1
    print(overlap)
