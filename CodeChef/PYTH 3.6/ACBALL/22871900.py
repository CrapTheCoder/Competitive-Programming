for _ in range(int(input())):
    x = input()
    y = input()

    for i in range(len(x)):
        if x[i] == 'B' and y[i] == 'B':
             print('W', end='')
        else:
             print('B', end='')

    print()