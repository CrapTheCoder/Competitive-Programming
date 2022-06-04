for _ in range(int(input())):
    s = input()
    n = len(s)

    print('YES' if sorted(s[:n//2]) == sorted(s[n//2+n%2:]) else 'NO')