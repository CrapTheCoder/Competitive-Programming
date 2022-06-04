for _ in range(int(input())):
    n, k = map(int, input().split())
    n = list(map(int, list(str(n))))

    for _ in range(k):
        if n[n.index(min(n))] == 9:
            break

        n[n.index(min(n))] += 1


    f = 1

    for i in n:
        f *= i

    print(f)