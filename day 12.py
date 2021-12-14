with open("day 12.txt") as file:
    content = file.read().splitlines()
    data = []
    for line in content:
        list = line.split("-")
        data.append(list)
    caves = {}
    for pair in data:
        if pair[0] not in caves.keys():
            caves[pair[0]] = [pair[1]]
        else:
            caves[pair[0]].append(pair[1])
        if pair[1] not in caves.keys():
            caves[pair[1]] = [pair[0]]
        else:
            caves[pair[1]].append(pair[0])

    print(caves)
    # Puzzle 1
    # def move():
    #     if path[-1] != "end":
    #         for entry in caves[path[-1]]:
    #             if entry.isupper() or entry not in path:
    #                 path.append(entry)
    #                 move()
    #                 path.pop()
    #     else:
    #         paths.append(path.copy())
    #
    #
    # paths = []
    # path = ["start"]
    # move()

    # Puzzle 2
    def move():
        if path[-1] != "end":
            for entry in caves[path[-1]]:
                if (entry != "start" and small_cave_once(path)) and (entry.isupper() or path.count(entry) < 2):
                    path.append(entry)
                    move()
                    path.pop()
        else:
            paths.append(path.copy())

    def small_cave_once(x):
        small_caves = [cave for cave in x if cave.upper() != cave]
        return len(small_caves) - len(set(small_caves)) <= 1

    paths = []
    path = ["start"]
    small_cave = []
    move()
    print(paths)
    print(len(paths))