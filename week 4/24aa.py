with open("24input", "r") as file:
    code = file.readlines()

num = [9, 9, 9, 2, 9, 9, 9, 5]

def search(num):
    if len(num) == 14:
        result = check(num)
        if result:
            return num
        else:
            return None

    elif None in num:
        i = num.index(None)
        for j in range(9, 0, -1):
            numm = num.copy()
            numm[i] = j
            result = search(numm)
            if result is not None:
                return result
        return None

    else:
        for i in range(9, 0, -1):
            result = search(num + [i])
            if result is not None:
                return result
        return None

def check(num):
    num = num[::-1]
    vars = {"w":0, "x":0, "y":0, "z":0}
    for line in code:
        line = line[:-1].split()
        if len(line) == 3:
            if line[2] in "wxyz":
                line[2] = vars[line[2]]
            else:
                line[2] = int(line[2])

        if line[0] == "inp":
            vars[line[1]] = num.pop()
        elif line[0] == "add":
            vars[line[1]] += line[2]
        elif line[0] == "mul":
            vars[line[1]] *= line[2]
        elif line[0] == "div":
            vars[line[1]] //= line[2]
        elif line[0] == "mod":
            vars[line[1]] %= line[2]
        elif line[0] == "eql":
            vars[line[1]] = int(vars[line[1]] == line[2])

    if vars["z"] == 0:
        return True
    else:
        return False

print(search(num))
