for _ in range(int(input())):
    s = input()

    stack = []
    a = [-1 for i in range(len(s))]
    l = -1

    for i in range(len(s) - 1, -1, -1):
        if s[i] == ')':
            stack.append(i)
            a[i] = l
        else:
            if stack:
                l = a[i] = stack.pop()
            else:
                l = -1

    q = int(input())

    for i in list(map(int, input().split())):
        if a[i - 1] == -1:
            print(-1)
        else:
            print(a[i - 1] + 1)