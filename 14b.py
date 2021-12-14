with open("14in.txt", "r") as file:
    string = file.readline()[:-1]
    file.readline()
    a = {key: val for key, val in [line[:-1].split(" -> ") for line in file]}
    counts = {a[key]: 0 for key in a}

    from matrix.matrix import Matrix
    m = Matrix(len(a), len(a), identity=False)
    strtoint = {}
    i = 0
    for key in a:
        strtoint[key] = i
        i += 1
    for key in a:
        val = a[key]
        m[strtoint[key[0] + val]][strtoint[key]] += 1
        m[strtoint[val + key[1]]][strtoint[key]] += 1

    m40 = m**40
    first = Matrix(len(a), 1, data=[[0] for i in range(len(a))])
    for i in range(len(string)-1):
        first[strtoint[string[i:i+2]]][0] += 1
    result = m40*first

    for key in a:
        num = result[strtoint[key]][0]
        counts[key[0]] += num
        counts[key[1]] += num
    counts[string[0]] += 1
    counts[string[-1]] += 1

    max = float("-inf")
    min = float("inf")
    for letter in counts:
        if counts[letter] > max:
            max = counts[letter]
        if counts[letter] < min:
            min = counts[letter]

    print((max - min)//2)
