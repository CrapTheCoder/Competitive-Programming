for _ in range(int(input())):
    s = input()
    n = len(s)
    
    x = 0
    y = 0
    
    if n % 2:
        print('no')
    else:
        for i, j in enumerate(s):
            if j == s[i-1] == 'R':
                if x == 1:
                    print('no')
                    break
                x += 1
                
            if j == s[i-1] == 'G':
                if y == 1:
                    print('no')
                    break
                y += 1

        else:
            print('yes')