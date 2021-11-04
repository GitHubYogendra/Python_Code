alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]
number = int(input())
for i in range(0, number):
    nameLi = []
    name = input().lower()
    pos = 0
    pos1 = 0
    total = []
    res = 0
    for n in name:
        nameLi.append(n)
        nameLi.sort()
    for n in nameLi:
        pos = alphabet.index(n) + 1
        pos1 = nameLi.index(n) + 1
        sump = pos * pos1
        total.append(sump)
        res = sum(total)

    print(res)

