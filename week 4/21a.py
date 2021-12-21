start = (7-1, 3-1)
#start = (4-1, 8-1)

rolls = 0
def roll():
    global rolls
    rolls += 3
    return (rolls - 3)%100 + (rolls - 2)%100 + (rolls - 1)%100 + 3

points = [0, 0]
pos = list(start)

player = 0
while points[0] < 1000 and points[1] < 1000:
    spaces = roll()
    pos[player] = (pos[player] + spaces)%10
    points[player] += pos[player] + 1
    player = int(not player)

print(points[player], rolls, points[player]*rolls)
