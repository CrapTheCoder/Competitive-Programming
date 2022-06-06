for _ in range(int(input())):
    s = input()
 
    print(len(s.replace('0', '')))
 
    for i, j in enumerate(s[::-1]):
        if j != '0':
            print(j + '0' * i, end=' ')
 
    print()