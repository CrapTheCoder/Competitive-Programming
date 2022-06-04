for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input()
    a = "abcdefghijklmnopqrstuvwxyz"

    counts = {}

    for char in s:
        if char not in counts:
            counts[char] = 0

        counts[char] += 1

    for i in range(q):
        c = int(input())
        t = 0
        for j in a:
            if j in counts and counts[j] - c > 0:
                t += counts[j] - c
        print(t)