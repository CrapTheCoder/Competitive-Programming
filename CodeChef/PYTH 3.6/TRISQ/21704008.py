for _ in range(int(input())):
    base = int(input())

    base -= 2
    base //= 2

    print(base * (base + 1) // 2)