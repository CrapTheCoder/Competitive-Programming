for _ in range(int(input())):
    a = input().strip()
    b = set(input().strip())

    ns = ''

    for i in a:
        if i not in b:
            ns += i

    print(ns)