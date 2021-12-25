data = []
with open("25in.txt", "r") as file:
    for line in file:
        data.append(list(line[:-1]))

steps = 0
changed = True
while changed:
    steps += 1
    changed = 0
    update = []
    for r in range(len(data)):
        for s in range(len(data[r])):
            if (data[r][s] == ">") and (data[r][(s+1)%len(data[r])] == "."):
                update.append((r, s))
    for r, s in update:
        data[r][s] = "."
        data[r][(s+1)%len(data[r])] = ">"
    changed += len(update)
    update = []
    for r in range(len(data)):
        for s in range(len(data[r])):
            if (data[r][s] == "v") and (data[(r+1)%len(data)][s] == "."):
                update.append((r, s))
    for r, s in update:
        data[r][s] = "."
        data[(r+1)%len(data)][s] = "v"
    changed += len(update)

print(steps)
