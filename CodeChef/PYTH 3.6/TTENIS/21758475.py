for _ in range(int(input())):
    s = input()

    a = s.count('0')
    b = len(s) - a

    if a < b: print('WIN')
    else: print('LOSE')