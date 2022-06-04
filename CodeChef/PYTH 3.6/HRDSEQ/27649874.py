r = [0]
l = 1

for i in range(130):
    for i in range(l - 2, -1, -1):
        if r[i] == r[-1]:
            r.append(l - 1 - i)
            break
    else:
        r.append(0)

    l += 1

for _ in range(int(input())):
    n = int(input())

    print(r[:n].count(r[n-1]))