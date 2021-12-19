with open("17in.txt", "r") as file:
    target = file.readline().strip("target area: x=").split(", y=")
    target = tuple(tuple(map(int, text.split(".."))) for text in target)

maxsteepness = - target[1][0] - 1
steps = 2*(maxsteepness + 1)

works = False
for i in range(steps):
    if target[0][0] <= (i*(i+1))//2 <= target[0][1]:
        works = True
        break

if works:
    print((maxsteepness*(maxsteepness+1)//2))
else:
    print("není")
