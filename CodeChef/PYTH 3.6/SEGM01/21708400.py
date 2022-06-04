for _ in range(int(input())):
    s = input().lstrip('0')
    x = 1

    if '1' not in s:
        print('NO')
    else:
        for i in s:
            if i == '0':
                x = 0
            else:
                if x == 0:
                    print('NO')
                    break
        else:
            print('YES')