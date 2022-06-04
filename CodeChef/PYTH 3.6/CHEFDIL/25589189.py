for _ in range(int(input())):
    s = input()
    c = s.count('1')

    if bool(c % 2):
        print('WIN')
    else:
        print('LOSE')