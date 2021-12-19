inf = float("inf")
with open("15in.txt", "r") as file:
    risk = []
    for line in file:
        row = [int(x) for x in line[:-1]]
        j = len(row)
        risk.append([inf] + 5*row + [inf])
    i = len(risk)
    risk = [[inf for _ in range(len(risk[0]))]] + 5*risk + [[inf for _ in range(len(risk[0]))]]

    from heapq import *
    q = [(0, (1, 1))]
    visited = {(1, 1): True}
    goal = (len(risk)-2, len(risk[0])-2)
    while q:
        dist, pos = heappop(q)
        if pos[0] <= 0 or pos[1] <= 0:
            print(pos, dist)
        if pos == goal:
            break
        for dir in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            npos = (pos[0] + dir[0], pos[1] + dir[1])
            if visited.get(npos, False):
                continue
            visited[npos] = True
            if risk[npos[0]][npos[1]] == inf:
                continue
            danger = ( risk[npos[0]][npos[1]] + (npos[0]-1)//i + (npos[1]-1)//j - 1)%9 + 1
            heappush(q, (dist + danger, npos))
    print(dist)
