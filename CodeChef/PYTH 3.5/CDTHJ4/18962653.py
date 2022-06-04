t = int(input())

for i in range(t):
    flagl = []
    pp, pl, ch, np = map(int, input().split())

    for j in range(np):
        pn, cn = map(int, input().split())
        if (pp <= (pn + pl)) and (cn <= ch):
            flag = True
            flagl.append(flag)
        else:
            flag = False
            flagl.append(flag)

    if True in flagl:
        print("Found")
    else:
        print("Not Found")