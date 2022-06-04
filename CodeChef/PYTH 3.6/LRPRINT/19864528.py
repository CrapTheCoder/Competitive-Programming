for _ in range(int(input())):
    s = input()

    upper = ''
    lower = ''

    for i in s:
        if i.isupper():
            upper += i
        else:
            lower += i

    print(upper + lower)