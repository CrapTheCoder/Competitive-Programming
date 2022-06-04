for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())

    ans = []

    for i in range(n):
        s = {i}

        for j in range(n):
            if a[i] == b[j] and a[i] < a[j]:
                s.add(j)
                a[j] = a[i]

        if len(s) == 1:
            continue

        ans.append((len(s), *s))

    if a == b:
        print(len(ans))

        for i in ans:
            print(*i)

    else:
        print(-1)
