with open("10in.txt", "r") as file:
    scores = []
    pairing = {"(":")", "[":"]", "{":"}", "<":">"}
    scoring = {")":1, "]":2, "}":3, ">":4}
    for line in file:
        pain = False
        line = line[:-1]
        stack = []
        for char in line:
            if char in pairing:
                stack.append(char)
            elif char == pairing[stack[-1]]:
                stack.pop()
            else:
                pain = True
                break
        if pain:
            continue


        score = 0
        while stack:
            char = stack.pop()
            score *= 5
            score += scoring[pairing[char]]
        scores.append(score)

    scores.sort()
    print(scores[len(scores)//2])
