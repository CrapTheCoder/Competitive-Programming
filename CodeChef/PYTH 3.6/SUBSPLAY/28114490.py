for _ in range(int(input())):
    n = int(input())
    s = input()

    d = {chr(i): -1 for i in range(97, 97 + 26)}

    m = 0

    for i in range(n):
        if d[s[i]] != -1:
            x = d[s[i]] + n - i

            if x > m:
                m = x

        d[s[i]] = i

    print(m)
