for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mini = float('inf')

    for i in a:
        c = 0

        while i % 2 == 0:
            i //= 2
            c += 1

        mini = min(mini, c)

    print(mini)