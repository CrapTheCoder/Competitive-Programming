for _ in range(int(input())):
    s = input()

    if max(s.count(i) for i in s) >= 2:
        print('yes')
    else:
        print('no')
