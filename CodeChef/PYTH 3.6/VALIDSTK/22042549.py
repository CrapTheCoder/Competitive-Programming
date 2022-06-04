for _ in range(int(input())):
    n = int(input())
    e = 0

    for i in input().split():
        if i == '1': e += 1
        if i == '0': e -= 1

        if e < 0:
            print('Invalid')
            break
    else:
        print('Valid')