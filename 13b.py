def fold(dots, text):
    text = text.strip("\n").strip("fold along ")
    mode = text[0]
    num = int(text[2:])
    if mode == "y":
        l = len(dots) - 1
        while l > num:
            while len(dots[2*num - l]) < len(dots[l]):
                dots[2*num - l].append(" ")
            for i in range(len(dots[l])):
                if dots[l][i] != " ":
                    dots[2*num - l][i] = dots[l][i]
            dots.pop()
            l -= 1
    else:
        for row in dots:
            i = len(row) - 1
            while i > num:
                if row[i] != " ":
                    row[2*num - i] = row[i]
                row.pop()
                i -= 1

with open("13in.txt", "r") as file:
    dots = []
    for line in file:
        if line == "\n":
            break
        x, y = map(int, line.split(","))
        while len(dots) <= y:
            dots.append([])
        while len(dots[y]) <= x:
            dots[y].append(" ")
        dots[y][x] = "#"
    for line in file:
        fold(dots, line)

    print("\n".join(["".join(row) for row in dots]))
