with open("4in.txt", "r") as file:
    nums = list(map(int, file.readline().split(",")))
    boards = []
    for line in file:
        line = line[:-1].strip()
        if line == "":
            boards.append([])
            continue

        boards[-1].append(list(map(int, line.split())))

    scores = []
    for board in boards:
        for i in range(len(nums)):
            num = nums[i]

            # replace num with None
            for r in range(5):
                for s in range(5):
                    if board[r][s] == num:
                        board[r][s] = None

            # check for whole row or column of Nones
            win = False
            for r in range(5):
                found = True
                for s in range(5):
                    if board[r][s] is not None:
                        found = False
                win |= found
            for s in range(5):
                found = True
                for r in range(5):
                    if board[r][s] is not None:
                        found = False
                win |= found

            # count score
            if win:
                sum = 0
                for r in range(5):
                    for s in range(5):
                        if board[r][s] is not None:
                            sum += board[r][s]
                scores.append((i, sum*num))
                break

    scores.sort()
    print(scores[-1][1])
