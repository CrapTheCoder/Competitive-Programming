for _ in range(int(input())):
    s = list(input())
    dep = 0

    for i in range(len(s)-1, -1, -1):
        j = s[i]

        if not (j.isalnum() or j in '()'):
            c_dep = 0

            k = i

            while k:
                k += 1

                try:
                    if s[k] == '(':
                        c_dep += 1
                    if s[k] == ')':
                        c_dep -= 1
                except:
                    break

                s[k], s[k-1] = s[k-1], s[k]

                if not c_dep:
                    break

    print(''.join(i for i in s if i not in '()'))
