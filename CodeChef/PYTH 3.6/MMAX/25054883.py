for _ in range(int(input())):
    n = int(input())
    k = int(input())

    if n == 1:
        print(0)
    elif n == 2:
        print(k % 2)
    else:
        x = k % n
        a = 2 * min(x, abs(n - x))

        print(a - (x == n / 2))
