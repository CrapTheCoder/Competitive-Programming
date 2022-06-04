from string import ascii_lowercase

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    t = input().strip()

    mini = float('inf')

    for c in ascii_lowercase:
        r = 0
        y = s.replace('?', c)
        z = t.replace('?', c)

        for i, j in zip(y, z):
            if i == j:
                continue

            if (i in 'aeiou') != (j in 'aeiou'):
                r += 1
            else:
                r += 2

        if r < mini:
            mini = r

    print(mini)