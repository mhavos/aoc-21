with open("24in.txt", "r") as file:
    code = file.readlines()
    ps = [[int(code[19*i + line][:-1].split()[-1]) for line in (4, 5, 15)] for i in range(14)]

def check(num):
    z = []
    for i in range(14):
        w = num[i]
        p = ps[i]

        x = z[-1] + p[1]
        if p[0] == 26:
            z.pop()

        if x + p[1]
