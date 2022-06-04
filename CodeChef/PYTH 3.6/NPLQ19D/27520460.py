for _ in range(int(input())):
    a = input()

    print(''.join(sorted(set(a), key=a.index)))