im = []
with open("20in.txt", "r") as file:
    update = [x for x in file.readline()[:-1]]
    file.readline()
    for line in file:
        im.append([x for x in line[:-1]])

for i in range(50):
    newim = []
    for r in range(-1, len(im)+1):
        newim.append([])
        for s in range(-1, len(im[0])+1):
            num = ""
            for rr in (-1, 0, 1):
                if not (0 <= r + rr < len(im)):
                    num += "111" if (update[0]=="1" and i%2) else "000"
                    continue
                for ss in (-1, 0, 1):
                    if not (0 <= s + ss < len(im[0])):
                        num += "1" if (update[0]=="1" and i%2) else "0"
                        continue
                    num += im[r+rr][s+ss]
            newim[-1].append(update[int(num, 2)])
    im = newim

total = 0
for row in im:
    for cell in row:
        total += int(cell)
print(total)
