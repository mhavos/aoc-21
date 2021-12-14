with open("14in.txt", "r") as file:
    string = file.readline()[:-1]
    file.readline()
    a = {key: val for key, val in [line[:-1].split(" -> ") for line in file]}
    counts = {a[key]: 0 for key in a}

    for j in range(10):
        newstring = []
        for i in range(len(string)-1):
            newstring.append(string[i])
            newstring.append(a[string[i:i+2]])
        newstring.append(string[-1])
        string = "".join(newstring)

    for letter in string:
        counts[letter] += 1
    max, min = (float("-inf"), None), (float("inf"), None)
    for letter in counts:
        if counts[letter] > max[0]:
            max = (counts[letter], letter)
        if counts[letter] < min[0]:
            min = (counts[letter], letter)
    print(max[0] - min[0])
