for _ in range(int(input())):
    s = input()

    if 1 in [s.count('0'), s.count('1')]:
        print('Yes')
    else:
        print('No')