with open("9in.txt", "r") as file:
    data = []
    for line in file:
        if len(data) == 0:
            data.append([float("inf") for _ in range(len(line) + 1)])
        data.append([float("inf")] + list(map(int, line[:-1])) + [float("inf")])
    data.append([float("inf") for _ in range(len(line) + 1)])

    total = 0
    for r in range(1, len(data)-1):
        for s in range(1, len(data[r])-1):
            lowest = True
            for dir in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if data[r][s] >= data[r + dir[0]][s + dir[1]]:
                    lowest = False
            if lowest:
                total += data[r][s] + 1
    print(total)
