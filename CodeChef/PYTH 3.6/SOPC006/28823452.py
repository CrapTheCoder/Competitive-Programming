for _ in range(int(input())):
    n = int(input())
    a = sorted(zip(list(map(int, input().split())), list(range(n))))

    i = 0

    c = 0

    v = []

    while i < n:
        if i >= n - 1:
            break

        if a[i][0] * 2 >= a[i + 1][0]:
            c += 1

            v.append((a[i][1] + 1, a[i+1][1] + 1))

            i += 2

        else:
            i += 1

    print(c * 2)

    for i in v:
        print(*i)