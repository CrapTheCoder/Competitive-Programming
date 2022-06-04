for _ in range(int(input())):
    n = int(input())
    n //= 2

    print(n * (n-1) // 2)