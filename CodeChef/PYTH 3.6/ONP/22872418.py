for _ in range(int(input())):
    l = []
    for c in list(input()):
        if c in '+-*/^(':
            l.append(c)
        elif c == ')':
            print(l.pop(), end='')
            l.pop()
        else:
            print(c, end='')

    print()