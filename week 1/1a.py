with open("input.txt", "r") as file:
    total = 0
    last = float("inf")
    for line in file:
        next = int(line)
        total += (next > last)
        last = next
    print(total)
