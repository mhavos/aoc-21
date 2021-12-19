i = 0
def parse(bin):
    global i
    V = int(bin[i:i+3], 2)
    T = int(bin[i+3:i+6], 2)
    i += 6
    if T == 4:
        # literal handling
        literal = []
        while True:
            literal.append(bin[i+1:i+5])
            i += 5
            if bin[i-5] == "0":
                break
        literal = "".join(literal)
        literal = int(literal, 2)

        return V
    else:
        # operator handling
        I = bin[i]
        i += 1
        if I == "0":
            # 15 bit length
            L = int(bin[i:i+15], 2)
            i += 15
            end = i + L
            while i < end:
                V += parse(bin)

            return V
        else:
            # 11 bit packet num
            L = int(bin[i:i+11], 2)
            i += 11
            for _ in range(L):
                V += parse(bin)

            return V

with open("16in.txt", "r") as file:
    hex = file.readline()[:-1]
hex = "620080001611562C8802118E34"

hextobin = {
    "0":"0000", "1":"0001", "2":"0010", "3":"0011",
    "4":"0100", "5":"0101", "6":"0110", "7":"0111",
    "8":"1000", "9":"1001", "A":"1010", "B":"1011",
    "C":"1100", "D":"1101", "E":"1110", "F":"1111",
}
bin = "".join([hextobin[x] for x in hex])

print(parse(bin))
