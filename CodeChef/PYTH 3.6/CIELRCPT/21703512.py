for _ in range(int(input())):
    n = int(input())

    if n < 4096:
        print(bin(n).count('1'))
    else:
        print(n // 2048 + bin(n % 2048).count('1'))
