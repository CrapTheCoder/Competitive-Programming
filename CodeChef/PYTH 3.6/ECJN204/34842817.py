for _ in range(int(input())):
    n = int(input())

    c = [0, 0, 0]

    for _ in range(n):
        x = input().split()

        for i in range(3):
            for j in range(3):
                if x[i] == 'R' and x[j] == 'P': c[i] -= 1
                if x[i] == 'P' and x[j] == 'R': c[i] += 1

                if x[i] == 'P' and x[j] == 'S': c[i] -= 1
                if x[i] == 'S' and x[j] == 'P': c[i] += 1

                if x[i] == 'S' and x[j] == 'R': c[i] -= 1
                if x[i] == 'R' and x[j] == 'S': c[i] += 1

    print(*c)
