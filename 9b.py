from collections import deque

with open("9in.txt", "r") as file:
    data = []
    for line in file:
        if len(data) == 0:
            data.append([float("inf") for _ in range(len(line) + 1)])
        data.append([float("inf")] + list(map(int, line[:-1])) + [float("inf")])
    data.append([float("inf") for _ in range(len(line) + 1)])

    basins = []
    for r in range(1, len(data)-1):
        for s in range(1, len(data[r])-1):
            lowest = True
            for dir in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if data[r][s] >= data[r + dir[0]][s + dir[1]]:
                    lowest = False
            if lowest:
                basins.append((r, s))

    for i in range(len(basins)):
        r, s = basins[i]
        data[r][s] = 9
        size = 1
        l = deque()
        l.append((r, s))
        while l:
            r, s = l.popleft()
            for dir in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if data[r + dir[0]][s + dir[1]] >= 9:
                    continue
                else:
                    data[r + dir[0]][s + dir[1]] = 9
                    l.append((r + dir[0], s + dir[1]))
                    size += 1
        basins[i] = size

    basins.sort()
    print( basins[-1]*basins[-2]*basins[-3] )
