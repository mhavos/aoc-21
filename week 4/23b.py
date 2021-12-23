a = [
    list("#############"),
    list("#.. . . . ..#"),
    list("###B#D#C#A###"),
    list("  #D#C#B#A#  "),
    list("  #D#B#A#C#  "),
    list("  #C#D#B#A#  "),
    list("  #########  ")
]

rooms = [[2, 3, 3, 1], [3, 1, 2, 3], [1, 0, 1, 2], [0, 2, 0, 0]]
#rooms = [[0, 3, 3, 1], [3, 1, 2, 2], [2, 0, 1, 1], [0, 2, 0, 3]]
slots = [None, None, rooms[0], None, rooms[1], None, rooms[2], None, rooms[3], None, None]

def copy(slots):
    return [(slots[i].copy() if i in (2, 4, 6, 8) else slots[i]) for i in range(len(slots))]
def can_enter(room, amphi):
    for num in room:
        if num != amphi:
            return False
    return True
def tupleize(slots):
    return tuple((tuple(slots[i]) if i in (2, 4, 6, 8) else slots[i]) for i in range(len(slots)))

class State:
    def __init__(self, cost, slots):
        self.cost = cost
        self.slots = slots

    def __lt__(self, other):
        return self.cost < other.cost

goal = [None, None, [0, 0, 0, 0], None, [1, 1, 1, 1], None, [2, 2, 2, 2], None, [3, 3, 3, 3], None, None]
debug = [
#    [None, None, [0, 3, 3, 1], None, [3, 1, 2, 2], None, [2, 0, 1, 1], None, [0, 2, 0], None, 3],
#    [0, None, [0, 3, 3, 1], None, [3, 1, 2, 2], None, [2, 0, 1, 1], None, [0, 2], None, 3]
]

from heapq import *
q = [State(0, slots)]
cache = {}

while q:
    state = heappop(q)
    cost, slots = state.cost, state.slots
    tup = tupleize(slots)
    if cache.get(tup, False) == True:
        continue
    else:
        cache[tup] = True

    if slots in debug:
        print(slots)

    if slots == goal:
        print("done")
        break

    for i in range(len(slots)):
        if type(slots[i]) == list:
            if len(slots[i]) == 0:
                continue

            amphi = slots[i][-1]
            exit = 5 - len(slots[i])
            for j in range(i+1, len(slots)):
                if slots[j] is None:
                    newslots = copy(slots)
                    newslots[j] = newslots[i].pop()
                    newcost = cost + 10**amphi * (exit + j-i)
                    heappush(q, State(newcost, newslots))
                elif type(slots[j]) == list:
                    if can_enter(slots[j], amphi) and (j//2 - 1 == amphi):
                        newslots = copy(slots)
                        newslots[j].append(newslots[i].pop())
                        enter = 5 - len(newslots[j])
                        newcost = cost + 10**amphi * (exit + j-i + enter)
                        heappush(q, State(newcost, newslots))
                else:
                    break
            for j in range(i-1, -1, -1):
                if slots[j] is None:
                    newslots = copy(slots)
                    newslots[j] = newslots[i].pop()
                    newcost = cost + 10**amphi * (exit + i-j)
                    heappush(q, State(newcost, newslots))
                elif type(slots[j]) == list:
                    if can_enter(slots[j], amphi) and (j//2 - 1 == amphi):
                        newslots = copy(slots)
                        newslots[j].append(newslots[i].pop())
                        enter = 5 - len(newslots[j])
                        newcost = cost + 10**amphi * (exit + i-j + enter)
                        heappush(q, State(newcost, newslots))
                else:
                    break

        elif slots[i] is not None:
            amphi = slots[i]
            for j in range(i+1, len(slots)):
                if type(slots[j]) == list:
                    if can_enter(slots[j], amphi) and (j//2 - 1 == amphi):
                        newslots = copy(slots)
                        newslots[j].append(newslots[i])
                        newslots[i] = None
                        enter = 5 - len(newslots[j])
                        newcost = cost + 10**amphi * (j-i + enter)
                        heappush(q, State(newcost, newslots))
                elif slots[j] is not None:
                    break
            for j in range(i-1, -1, -1):
                if type(slots[j]) == list:
                    if can_enter(slots[j], amphi) and (j//2 - 1 == amphi):
                        newslots = copy(slots)
                        newslots[j].append(newslots[i])
                        newslots[i] = None
                        enter = 5 - len(newslots[j])
                        newcost = cost + 10**amphi * (i-j + enter)
                        heappush(q, State(newcost, newslots))
                elif slots[j] is not None:
                    break

if slots == goal:
    print(cost)

#print(cache)
