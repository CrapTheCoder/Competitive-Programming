for _ in range(int(input())):
    n = int(input())
    a = list(zip(map(int, input().split()), range(n)))

    a.sort(key=lambda x: x[0], reverse=True)

    sol = [0] * n

    for i in range(n):
        sol[a[i][1]] = i+1

    print(*sol)