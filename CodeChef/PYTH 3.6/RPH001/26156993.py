for _ in range(int(input())):
    n, m = input().split()

    n = n[::-1]
    m = m[::-1]

    print(str(int(n) + int(m))[::-1].lstrip('0'))