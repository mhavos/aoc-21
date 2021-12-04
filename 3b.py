with open("3in.txt", "r") as file:
    data = [line[:-1] for line in file]
    resullt = {}

    for other in (False, True):
        i = 0
        oxygen = data.copy()
        while len(oxygen) > 1:
            ones = 0
            zeroes = 0
            for num in oxygen:
                if num[i] == "1":
                    ones += 1
                else:
                    zeroes += 1

            if (ones >= zeroes) ^ other:
                good = "1"
            else:
                good = "0"

            newoxygen = []
            for num in oxygen:
                if num[i] == good:
                    newoxygen.append(num)
            oxygen = newoxygen

            i += 1
        resullt[other] = oxygen[0]
    print(int(resullt[True], 2) * int(resullt[False], 2))
