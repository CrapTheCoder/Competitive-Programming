for _ in range(int(input())):
    s = input()
    c = s.count(max(s, key=s.count))

    print('YES' if c == (len(s) - c) else 'NO')