for _ in range(int(input())):
    s = input()
    n = len(s)

    a, b = s[:n//2], s[n//2+n%2:]

    print('YES' if sorted(a) == sorted(b) else 'NO')