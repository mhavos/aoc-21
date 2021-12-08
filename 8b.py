with open("8in.txt", "r") as file:
    total = 0
    for line in file:
        patterns, outs = line.split(" | ")
        patterns, outs = patterns.split(), outs.split()
        counts = {char:0 for char in "abcdefg"}
        reals = {}
        for pattern in patterns:
            for char in pattern:
                counts[char] += 1
            if len(pattern) == 2:
                one = pattern
            elif len(pattern) == 3:
                seven = pattern
            elif len(pattern) == 4:
                four = pattern

        for char in counts:
            if (char in seven) and (char not in one):
                reals[char] = "a"
            elif (counts[char] == 7) and (char in four):
                reals[char] = "d"
            else:
                reals[char] = {4:"e", 6:"b", 7:"g", 8:"c", 9:"f"}[counts[char]]

        num = ""
        lookup = {
            "abcefg": 0, "cf": 1,
            "acdeg": 2, "acdfg": 3,
            "bcdf": 4, "abdfg": 5,
            "abdefg": 6, "acf": 7,
            "abcdefg": 8, "abcdfg": 9
        }
        for out in outs:
            contains = [reals[char] for char in out]
            contains.sort()
            contains = "".join(contains)
            num += str(lookup[contains])

        total += int(num)
    print(total)
