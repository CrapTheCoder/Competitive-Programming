for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = 0

    if a <= 0 and b <= 0:
        if n % 2 == 0:
            s += a
        else:
            s += b

        print(s)

    else:
        even = False
        if n % 2 == 0:
            even = True

        if a <= 0:
            if n % 2 == 0:
                while n % 2 == 0:
                    n //= 2
                s += a

        else:
            while n % 2 == 0:
                s += a
                n //= 2

        if b <= 0:
            if not even:
                s += b

        else:
            for i in range(2, int(n ** 0.5) + 2):
                while n % i == 0:
                    n //= i
                    s += b

            if n > 1:
                s += b

        print(s)
