with open("7in.txt", "r") as file:
    l = list(map(int, file.readline().split(",")))
    l.sort()
    total = 0
    i = len(l)//2
    for num in l:
        total += abs(num - l[i])

    print(total)
