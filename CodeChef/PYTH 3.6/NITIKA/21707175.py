for _ in range(int(input())):
    a = input().title().split()

    if len(a) == 1:
        print(a[0])
    if len(a) == 2:
        print(a[0][0] + '. ' + a[1])
    if len(a) == 3:
        print(a[0][0] + '. ' + a[1][0] + '. ' + a[2])