for _ in range(int(input())):
    n = input()

    if n[-1] == '0':
        print(0)
    elif n[-1] == '5':
        print(1)
    else:
        print(-1)
