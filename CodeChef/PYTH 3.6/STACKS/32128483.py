import bisect

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    disks = []

    for e in a:
        i = bisect.bisect(disks, e)

        if i == len(disks):
            disks.append(e)
            continue

        if disks[i] == e:
            i += 1

        if i == len(a):
            disks.append(e)
            continue

        disks.pop(i)

        bisect.insort(disks, e)

    print(len(disks), *disks)
