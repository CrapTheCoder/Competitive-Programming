for _ in range(int(input())):
    s = input()
    x = ''

    for i in s:
        if i == '<': x += '>'
        if i == '>': x += '<'
        if i == '*': x += '*'

    print(x.count('><'))