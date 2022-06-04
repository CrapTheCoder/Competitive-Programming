t = int(input())

for x in range(t):
    ans = 0
    n = int(input())

    cl = map(int, input().split())

    for z in cl:
        ans += z

    if ans % 2 == 1:
        print("YES")
        continue

    else:
        print("NO")