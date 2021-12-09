vents = {}
def write(x1, y1, x2, y2):
    coords = []
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        coords = [(x1, i) for i in range(y1, y2+1)]
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        coords = [(i, y1) for i in range(x1, x2+1)]
    elif x2 - x1 == y2 - y1:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        coords = [(x1+i, y1+i) for i in range(x2-x1+1)]
    elif x2 - x1 == y1 - y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = max(y1, y2), min(y1, y2)
        coords = [(x1+i, y1-i) for i in range(x2-x1+1)]
    for coord in coords:
        if vents.get(coord[0], None) is None:
            vents[coord[0]] = {}
        if vents[coord[0]].get(coord[1], None) is None:
            vents[coord[0]][coord[1]] = 0
        vents[coord[0]][coord[1]] += 1

with open("5in.txt", "r") as file:
    for line in file:
        c1, c2 = line.split(" -> ")
        x1, y1 = list(map(int, c1.split(",")))
        x2, y2 = list(map(int, c2.split(",")))
        write(x1, y1, x2, y2)

#vis = ["."*10 for _ in range(10)]
count = 0
for x in vents:
    for y in vents[x]:
#        vis[y] = vis[y][:x] + str(vents[x][y]) + vis[y][x+1:]
        if vents[x][y] > 1:
            count += 1

#print("\n".join(vis))
print(count)
