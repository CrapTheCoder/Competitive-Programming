for _ in range(int(input())):
    a, b = map(int, input().split())

    i = 1
    j = 2

    while True:
        a -= i

        if a < 0:
            print('Bob')
            break

        b -= j

        if b < 0:
            print('Limak')
            break

        i += 2
        j += 2