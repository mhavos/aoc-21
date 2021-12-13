with open("8in.txt", "r") as file:
    total = 0
    for line in file:
        nums = line.split(" | ")[1].split()
        for num in nums:
            if len(num) in [2, 3, 4, 7]:
                total += 1

    print(total)
