for _ in range(int(input())):
    n = int(input())
    s = input()

    c = 0

    for i in s:
        if i == 'H': c += 1
        if i == 'T': c -= 1

        if c < 0 or c > 1:
            print('Invalid')
            break
    else:
        if c == 0:
            print('Valid')
        else:
            print('Invalid')
