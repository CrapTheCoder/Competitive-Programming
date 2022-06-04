from collections import defaultdict

for _ in range(int(input())):
    n, q = map(int, input().split())

    ind = defaultdict(list)
    occ = {}

    unique_val = 1
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1

        ind[l].append(unique_val)
        ind[r+1].append(-unique_val)
        unique_val += 1

    no_sts = 0
    ispeed = 0

    for i in range(n):
        for j in ind[i]:
            if j > 0:
                occ[j] = i
                ispeed += 1

            if j < 0:
                no_sts -= i - occ[-j]
                ispeed -= 1

        no_sts += ispeed

        print(no_sts, end=' ')

    print()
