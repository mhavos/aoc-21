data = []
with open("22in.txt", "r") as file:
    for line in file:
        action, coords = line.split()
        coords = [1 if action == "on" else 0, [[int(coord) for coord in dim.split("=")[1].split("..")] for dim in coords.split(",")]]
        data.append(coords)

data = data[::-1]
data.append([0, [[-50, 50], [-50, 50], [-50, 50]]])

total = 0
for x in range(-50, 51):
    for y in range(-50, 51):
        for z in range(-50, 51):
            for action in data:
                if (action[1][0][0] <= x <= action[1][0][1]) and (action[1][1][0] <= y <= action[1][1][1]) and (action[1][2][0] <= z <= action[1][2][1]):
                    total += action[0]
                    break

print(total)
