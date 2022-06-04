from sys import stdin
input = stdin.readline

INF = 10 ** 10

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    l2 = -1

    ans = [0] * n

    for i in range(n):
        if a[i] % 4 == 0:
            ans[i] += i + 1
            l2 = i

        elif a[i] % 2:
            if l2 != -1:
                ans[i] = ans[l2] + i - l2
            else:
                ans[i] += i + 1

        else:
            ans[i] += l2 + 1

            l2 = i

    print(sum(ans))
