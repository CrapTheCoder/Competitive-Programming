for _ in range(int(input())):
    n = input().strip()

    s = 0
    for i in n:
        s += int(i) ** len(n)

    if s == int(n):
        print('FEELS GOOD')
    else:
        print('FEELS BAD')