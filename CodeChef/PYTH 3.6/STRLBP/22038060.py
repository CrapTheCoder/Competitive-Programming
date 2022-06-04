for _ in range(int(input())):
    s = input()

    while '00' in s: s = s.replace('00', '0')
    while '11' in s: s = s.replace('11', '1')

    cou = sum(s[i-1] != j for i, j in enumerate(s))

    if cou < 3: print('uniform')
    else: print('non-uniform')