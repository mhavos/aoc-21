with open("10in.txt", "r") as file:
    total = 0
    pairing = {"(":")", "[":"]", "{":"}", "<":">"}
    scoring = {")":3, "]":57, "}":1197, ">":25137}
    for line in file:
        line = line[:-1]
        stack = []
        for char in line:
            if char in pairing:
                stack.append(char)
            elif char == pairing[stack[-1]]:
                stack.pop()
            else:
                total += scoring[char]
                break

    print(total)
