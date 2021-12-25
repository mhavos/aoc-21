with open("24input", "r") as file:
    code = file.readlines()

num = [9, 9, None, None, 9, 9, 9]

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
    A = (num[2] - 7 != num[3])
    B = (num[6] - 4 != num[7])
    C = (num[8] - 2 != num[9])
    D = ( (25*C + 1)*((25*B + 1)*(num[5] + 4) + (num[7] + 9)*B) + (num[9] + 13)*C )%26 - 12 != num[10]
    E = (25*D + 1)*((25*C + 1)*((25*B + 1)*(26*(26*(25*A + 1)*(26*(num[0] + 15) + num[1] + 8) + 26*(num[3] + 6)*A + (num[4] + 13)) + num[5] + 4) + (num[7] + 9)*B)/26) + (num[10] + 9)*D
    F = (E%26 - 10 != num[11])
    G = (25*F + 1)*((25*D + 1)*((25*C + 1)*((25*B + 1)*(26*(26*(25*A + 1)*(26*(num[0] + 15) + num[1] + 8) + 26*(num[3] + 6)*A + (num[4] + 13)) + num[5] + 4) + (num[7] + 9)*B)//26)//26) + (num[11] + 6)*F
    H = (G%26 - 1 != num[12])
    I = (( (G//26)*(25*H + 1) + (num[12] + 2)*H )%26 - 11 != num[13])

    w = (( (G//26)*(25*H + 1) + (num[12] + 2)*H )//26)*(25*I + 1) + (num[13] + 2)*I
    if w == 0:
        return num

print(search(num))
