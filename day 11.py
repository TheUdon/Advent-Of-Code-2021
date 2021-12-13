with open("day 11.txt") as file:
    line = file.readline()
    data = []
    while line:
        new_list = [int(x) for x in line.strip("\n")]
        data.append(new_list)
        line = file.readline()

    def flash():
        flashes = 0
        for x in range(10):
            for y in range(10):
                if data[x][y] > 9:
                    flashes += 1
                    data[x][y] = -10000000
                    offsets = [[x + 1, y + 1], [x - 1, y + 1], [x + 1, y - 1], [x - 1, y - 1], [x + 1, y], [x - 1, y],
                               [x, y + 1], [x, y - 1]]
                    for offset in offsets:
                        if (offset[0] < 0) or (offset[0] >= (len(data))) or (offset[1] < 0) or (offset[1] >= (len(data[x]))):
                            continue
                        else:
                            data[offset[0]][offset[1]] += 1
        return flashes


    def add_1():
        for x in range(10):
            for y in range(10):
                data[x][y] += 1


    def zero():
        for x in range(10):
            for y in range(10):
                if data[x][y] < 0:
                    data[x][y] = 0

    # Puzzle 1
    # total_flashes = 0
    # for step in range(100):
    #     add_1()
    #
    #     flashes = flash()
    #     while flashes > 0:
    #         total_flashes += flashes
    #         flashes = flash()
    #     zero()
    # print(total_flashes)

    # Puzzle 2
    loop = True
    step = 0
    while loop:
        total_flashes = 0
        add_1()

        flashes = flash()
        while flashes > 0:
            total_flashes += flashes
            flashes = flash()
        zero()
        if total_flashes == 100:
            loop = False
        step += 1
    print(step)