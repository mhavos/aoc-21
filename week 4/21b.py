start = (7-1, 3-1)
#start = (4-1, 8-1)

cache = {}
def simulate(pos, points):
    result = cache.get((pos, points), None)
    if result is not None:
        return result

    result = (0, 0)
    for r1 in range(1, 1+3):
        for r2 in range(1, 1+3):
            for r3 in range(1, 1+3):
                roll = r1 + r2 + r3
                newpos = (pos[1], (pos[0] + roll)%10)
                newpoints = (points[1], points[0] + newpos[1] + 1)
                if newpoints[1] < 21:
                    newresult = simulate(newpos, newpoints)
                else:
                    newresult = (0, 1)
                result = (result[0] + newresult[1], result[1] + newresult[0])

    cache[(pos, points)] = result
    return result

print(max(simulate(start, (0, 0))))
