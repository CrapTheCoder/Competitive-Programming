days = {'mon': 0, 'tues': 1, 'wed': 2, 'thurs': 3, 'fri': 4, 'sat': 5, 'sun': 6}

for _ in range(int(input())):
    n, m = input().split()
    n = int(n)

    o = [4, 4, 4, 4, 4, 4, 4]

    for i in range(days[m], days[m] + n - 28):
        o[i % 7] = 5

    print(*o)