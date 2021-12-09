with open("input.txt", "r") as file:
    total = 0
    inf = float("inf")
    last = [inf, inf, inf]
    for line in file:
        next = last[1:] + [int(line)]
        total += (sum(next) > sum(last))
        last = next
    print(total)
