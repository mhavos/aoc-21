from vector19 import Vector

data = []
with open("19in.txt", "r") as file:
    for line in file:
        if line[0:3] == "---":
            data.append([])
        elif line != "\n":
            data[-1].append(Vector(map(int, line.split(","))))

dists = []
for scannerid in range(len(data)):
    dists.append([])
    for j in range(len(data[scannerid])):
        for i in range(j):
            difference = data[scannerid][j] - data[scannerid][i]
            quadrance = difference.quadrance()
            dists[-1].append((quadrance, (i, j), difference))
    dists[-1].sort()

offset = {0:(Vector(0, 0, 0), Vector.transformations[0])}
todo = [0]
open = {i for i in range(1, len(data))}
while len(open):
    ida = todo.pop()
    print(f"finding overlaps of {ida}")
    for idb in open.copy():
        # compare scanners ida and idb
        done = False
        for qa, pa, da in dists[ida]:
            trans = offset[ida][1]
            da = data[ida][pa[1]].transform(trans) - data[ida][pa[0]].transform(trans)
            for qb, pb, db in dists[idb]:
                for swap in (False, True):
                    if swap:
                        pb = (pb[1], pb[0])
                        db = -db
                    if qa != qb:
                        continue
                    if da.similar_to(db):
                        transb = db.similar_to(da, True)
                    else:
                        continue

                    # count overlapping beacons by tranformation transb
                    absp0 = data[ida][pa[0]].transform(offset[ida][1]) + offset[ida][0]
                    offsetb = (absp0 - data[idb][pb[0]].transform(transb), transb)
                    total = 0
                    for beacon in data[idb]:
                        beacon = beacon.transform(offsetb[1]) + offsetb[0]
                        for x in data[ida]:
                            if beacon == x.transform(offset[ida][1]) + offset[ida][0]:
                                total += 1

                    if total < 12:
                        continue
                    # if they have at least 12 points in common, this is correct
                    print(f"{ida} and {idb} overlap: {idb} is offset by {offsetb[0]} from 0")
                    offset[idb] = offsetb
                    todo.append(idb)
                    open.remove(idb)
                    done = True
                if done:
                    break

all = set()
for id in range(len(data)):
    for beacon in data[id]:
        all.add(beacon.transform(offset[id][1]) + offset[id][0])

maxdist = 0
for ida in range(len(data)):
    for idb in range(ida):
        d = offset[ida][0] - offset[idb][0]
        dist = abs(d[0]) + abs(d[1]) + abs(d[2])
        maxdist = max(dist, maxdist)
print(maxdist)
