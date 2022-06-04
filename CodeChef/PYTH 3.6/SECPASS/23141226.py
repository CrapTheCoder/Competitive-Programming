for _ in range(int(input())):
    n = int(input())
    s = input() + ' '
    seq = [i for i in range(1, n) if s[i] == s[0]]

    if not seq:
        print(s)
    else:
        flag, temp = 1, None

        for i in range(1, seq[0] + 1):
            if flag:
                for y in seq:
                    if s[y + i] != s[i]:
                        temp, flag = i, 0
                        break
            else:
                temp = i - 1
                break

        print(s[:temp])