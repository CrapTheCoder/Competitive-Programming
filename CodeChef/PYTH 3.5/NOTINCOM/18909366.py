def setint(set1, set2):
    ans = set(set1).intersection(set2)

    anslen = ans.__len__()
    print(anslen)

    return ans

tes = int(input())

for h in range(tes):
    albe = input().split()

    list(albe)

    a = int(albe[0])
    b = int(albe[1])

    al = input().split()
    be = input().split()

    list(al)
    list(be)

    setint(al, be)