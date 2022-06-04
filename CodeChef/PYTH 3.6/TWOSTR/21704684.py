for _ in range(int(input())):
    a = input()
    b = input()

    min = 0
    max = 0

    for i, j in zip(a, b):
        if i != j and ('?' not in [i, j]):
            print('No')
            break
    else:
        print('Yes')