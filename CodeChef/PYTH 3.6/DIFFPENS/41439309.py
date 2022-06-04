from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    c = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            c += 1

    print(c)