with open("2in.txt", "r") as file:
    horizontal = 0
    depth = 0
    aim = 0
    for line in file:
        dir, dist = line.split()
        dist = int(dist)
        if dir == "forward":
            horizontal += dist
            depth += aim * dist
        elif dir == "down":
            aim += dist
        else:
            aim -= dist
    print(horizontal * depth)
