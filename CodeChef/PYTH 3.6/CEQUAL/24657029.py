for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = {}

    for i in a:
        d[i] = d.get(i, 0) + 1

    for i in d.values():
        if i > 1:
            print('Yes')
            break
    else:
        print('No')

