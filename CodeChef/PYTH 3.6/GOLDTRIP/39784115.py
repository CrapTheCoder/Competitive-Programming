for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    p = [0]
    for i in a:
        p.append(p[-1] + i)

    for _ in range(int(input())):
        l, r = map(int, input().split())
        print(p[r] - p[l-1])