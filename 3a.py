with open("3in.txt", "r") as file:
    line = file.readline()
    ones = [int(x) for x in line[:-1]]
    zeroes = [1 - int(x) for x in line[:-1]]
    for line in file:
        for i in range(len(line) - 1):
            x = line[:-1][i]
            ones[i] += int(x == "1")
            zeroes[i] += int(x == "0")
    total = ["", ""]
    for i in range(len(ones)):
        if ones[i] >= zeroes[i]:
            total[0] += "1"
            total[1] += "0"
        else:
            total[1] += "1"
            total[0] += "0"
    print(int(total[0], 2) * int(total[1], 2))
