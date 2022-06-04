d = {
    1: 1,
    2: 7,
    3: 8,
    4: 5,
    5: 4,
    6: 9,
    7: 2,
    8: 3,
    9: 6
}

for _ in range(int(input())):
    s = list(input())
    n = len(s)

    if '0' in s:
        print('false')
        continue

    if n % 2:
        del s[n // 2]
        n -= 1

    for i in range(n // 2):
        if int(s[i]) != d[int(s[n - i - 1])]:
            print('false')
            break
    else:
        print('true')
