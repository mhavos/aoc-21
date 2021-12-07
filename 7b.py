def calculate(mean):
    total = 0
    for num in l:
        total += abs(num - mean)*(abs(num - mean) + 1)//2
    return total

with open("7in.txt", "r") as file:
    l = list(map(int, file.readline().split(",")))
    fmean = sum(l)//len(l)
    ts = [calculate(fmean - 1), calculate(fmean), calculate(fmean + 1)]
    while True:
        if ts[0] >= ts[1] <= ts[2]:
            best, total = fmean, ts[1]
            break

        if ts[0] < ts[2]:
            fmean -= 1
            ts = [calculate(fmean - 1)] + ts[:2]
        else:
            fmean += 1
            ts = ts[1:] + [calculate(fmean + 1)]

    print(best, total)
