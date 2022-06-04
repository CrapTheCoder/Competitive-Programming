for _ in range(int(input())):
    s = input()
    x = s.count('0')
    y = s.count('1')

    if len(s) % 2 or (not x) or (not y):
        print(-1)
        continue

    print(abs(x - y) // 2)
