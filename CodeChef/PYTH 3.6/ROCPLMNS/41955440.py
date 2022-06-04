MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    maxi = 0

    cur = 0
    for i in s:
        if i == '+': cur += 1
        if i == '-': cur -= 1

        if cur < 0:
            cur = 0

        maxi = max(maxi, cur)

    print(maxi)