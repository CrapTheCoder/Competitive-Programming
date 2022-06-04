for _ in range(int(input())):
    k, n = map(int, input().split())
    a = input().split()

    c = 0

    for i in range(n):
        if a[i] == 'S':
            x = []

            for j in range(max(i-k, 0), min(i+k+1, n)):
                if a[j] == 'N':
                    x.append(j)

            if x:
                a[x[0]] = 'X'
                c += 1

    print(c)
