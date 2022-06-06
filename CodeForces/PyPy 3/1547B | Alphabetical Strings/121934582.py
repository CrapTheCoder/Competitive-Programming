from string import ascii_lowercase
 
for _ in range(int(input())):
    s = input().strip()
    t = sorted(s)
 
    for i in range(len(t)):
        if t[i] != ascii_lowercase[i]:
            print('NO')
            break
 
    else:
        left = s.index('a') - 1
        right = s.index('a') + 1
 
        for i in range(1, len(s)):
            if 0 <= left and s[left] == ascii_lowercase[i]:
                left -= 1
                continue
 
            if right < len(s) and s[right] == ascii_lowercase[i]:
                right += 1
                continue
 
            break
 
        else:
            print('YES')
            continue
 
        print('NO')