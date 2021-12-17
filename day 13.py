with open("day 13.txt") as file:
    # Folding concept
    # Puzzle 1
    content = file.read().splitlines()
    content = [i.split() for i in content]
    dots = []
    fold_instructions = []
    for x in content:
        if x == []:
            pass
        elif x[0] != "fold":
            split = x[0].split(",")
            dots.append([int(split[0]), int(split[1])])
        elif "fold" in x:
            fold = x[2].split("=")
            fold_instructions.append([fold[0], int(fold[1])])

    def fold_x(dots, xfold):
        after = set()
        for point in dots:
            if point[0] > xfold:
                p = (xfold - (point[0] - xfold), point[1])
                after.add(p)
            else:
                p = (point[0], point[1])
                after.add(p)
        return after

    # print(fold_instructions[0][1])
    # points = fold_x((fold_instructions[0][1]))
    # count = len(points)
    # print(count)

    # Puzzle 2

    def fold_y(dots, yfold):
        after = set()
        for point in dots:
            if point[1] > yfold:
                p = (point[0], yfold - (point[1] - yfold))
                after.add(p)
            else:
                p = (point[0], point[1])
                after.add(p)
        return after

    for fold in fold_instructions:
        if fold[0] == "x":
            dots = fold_x(dots, fold[1])
        else:
            dots = fold_y(dots, fold[1])

    print(dots)
    grid = []
    x_list = [x[0] for x in dots]
    y_list = [y[1] for y in dots]
    max_x = max(x_list)
    max_y = max(y_list)
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(".")
        grid.append(row)

    for dot in dots:
        grid[dot[1]][dot[0]] = "X"

    for y in grid:
        for x in y:
            print(x, end=" ")
        print()