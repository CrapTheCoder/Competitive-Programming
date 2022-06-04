from itertools import combinations

for _ in range(int(input())):
    n, m = map(int,input().split())
    a = [int(input()) for i in range(n)]
    c = [sum(i) for h in range(n + 1) for i in combinations(a, h)]

    if m in c:
        print('Yes')
    else:
        print('No')