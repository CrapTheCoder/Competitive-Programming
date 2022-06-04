for _ in range(int(input())):
    s = input().strip()

    if (len(s) != 10) or s.startswith('0') or any(not i.isdigit() for i in s):
        print('NO')
        continue

    print('YES')
