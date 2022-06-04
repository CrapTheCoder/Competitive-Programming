for _ in range(int(input())):
    n = int(input())
    on = n

    coords = []

    for _ in range(n):
        x, y = map(int, input().split())
        coords.append([x, y])

    sol = 0

    while True:
        n //= 2

        if n < 3:
            print(sol + on)
            break

        sol += n
