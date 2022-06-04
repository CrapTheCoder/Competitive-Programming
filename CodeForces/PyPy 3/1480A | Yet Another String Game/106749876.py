for _ in range(int(input())):
    s = input()
 
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'a':
                print('b', end='')
            else:
                print('a', end='')
        else:
            if s[i] == 'z':
                print('y', end='')
            else:
                print('z', end='')
 
    print()