inf = float("inf")
with open("15in.txt", "r") as file:
    risk = []
    for line in file:
        risk.append([inf] + [int(x) for x in line[:-1]] + [inf])
    risk = [[inf for _ in range(len(risk[0]))]] + risk + [[inf for _ in range(len(risk[0]))]]

    from heapq import *
    q = [(0, (1, 1))]
    visited = {(1, 1): True}
    goal = (len(risk)-2, len(risk[0])-2)
    while q:
        dist, pos = heappop(q)
        if pos == goal:
            break
        for dir in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            npos = (pos[0] + dir[0], pos[1] + dir[1])
            if visited.get(npos, False):
                continue
            visited[npos] = True
            heappush(q, (dist + risk[npos[0]][npos[1]], npos))
    print(dist)
