from string import ascii_uppercase

for _ in range(int(input())):
    n = int(input())

    cur = ['*'] * n
    c = 0

    for i in range(n):
        d = cur.copy()
        for j in range((i+1) % 2, n, 2):
            d[j] = ascii_uppercase[c]
            c += 1

        print(*d, sep='')