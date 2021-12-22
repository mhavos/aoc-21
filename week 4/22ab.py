options = [set(), set(), set()]
inf = float("inf")

data = []
with open("22in.txt", "r") as file:
    for line in file:
        action, coords = line.split()
        coords = [1 if action == "on" else 0, [[int(dim.split("=")[1].split("..")[0]), int(dim.split("=")[1].split("..")[1])+1] for dim in coords.split(",")]]
        data.append(coords)
        for i in range(3):
            for j in range(2):
                options[i].add(data[-1][1][i][j])

data = data[::-1]
data.append([0, [[-inf, inf], [-inf, inf], [-inf, inf]]])

options = list(map(list, options))
options[0].sort(); options[1].sort(); options[2].sort()

total = 0
for i in range(len(options[0])-1):
    x = options[0][i] + 0.5
    for j in range(len(options[1])-1):
        y = options[1][j] + 0.5
        for k in range(len(options[2])-1):
            z = options[2][k] + 0.5
            for action in data:
                volume = (options[0][i+1] - options[0][i])*(options[1][j+1] - options[1][j])*(options[2][k+1] - options[2][k])
                if (action[1][0][0] <= x <= action[1][0][1]) and (action[1][1][0] <= y <= action[1][1][1]) and (action[1][2][0] <= z <= action[1][2][1]):
                    total += action[0] * volume
                    break

print(total)
