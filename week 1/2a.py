with open("2in.txt", "r") as file:
    total = {"forward":0, "down":0, "up":0}
    for line in file:
        dir, dist = line.split()
        total[dir] += int(dist)
    print(total["forward"] * (total["down"] - total["up"]))
