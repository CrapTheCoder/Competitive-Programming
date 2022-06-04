for _ in range(int(input())):
    l = input()

    n = len(l)
    m, s = l.count('m'), l.count('s')

    i = 0

    while i < n - 1:
        if l[i] != l[i+1]:
            i += 1
            s -= 1
        i += 1

    if m > s:
        print('mongooses')
    elif m < s:
        print('snakes')
    else:
        print('tie')