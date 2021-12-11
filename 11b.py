def get_adjacent(pos):
    i, j = pos
    adj = []
    for dir in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
        if (0 <= i + dir[0] < r) and (0 <= j + dir[1] < s):
            adj.append((i + dir[0], j + dir[1]))
    return tuple(adj)

def update(data):
    count = 0
    flashes = {}
    stack = []
    for i in range(r):
        for j in range(s):
            data[i][j] += 1
            if data[i][j] == 10:
                count += 1
                stack.append((i, j))
    while stack:
        pos = stack.pop()
        for adj in get_adjacent(pos):
            data[adj[0]][adj[1]] += 1
            if data[adj[0]][adj[1]] == 10:
                count += 1
                stack.append(adj)

    for i in range(r):
        for j in range(s):
            if data[i][j] > 9:
                data[i][j] = 0

    return count

with open("11in.txt", "r") as file:
    data = [[int(num) for num in line[:-1]] for line in file]
    r, s = len(data), len(data[0])

i = 0
while True:
    i += 1
    count = update(data)
    if count == r*s:
        break

print(i)
