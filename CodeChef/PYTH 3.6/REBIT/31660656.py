pow2_50 = 1 << 50

MOD = 998244353

def inv(x):
    return pow(x, MOD - 2, MOD) % MOD

def div(x, y):
    return x * inv(y) % MOD

for _ in range(int(input())):
    h = input()

    signs = []
    values = []

    for i in h:
        if i == '#':
            values.append({0: 1, 1: 1})

        if i in '&|^':
            signs.append(i)

        if i == ')':
            sign = signs.pop()

            s2 = values.pop()
            s1 = values.pop()

            s3 = {}

            if sign == '&':
                s3[0] = (s1[0] * s2[0]) + (s1[0] * s2[1])  + (s1[1] * s2[0])
                s3[1] = (s1[1] * s2[1])

            if sign == '^':
                s3[0] = (s1[0] * s2[0]) + (s1[1] * s2[1])
                s3[1] = (s1[0] * s2[1]) + (s1[1] * s2[0])

            if sign == '|':
                s3[0] = (s1[0] * s2[0])
                s3[1] = (s1[1] * s2[1]) + (s1[0] * s2[1]) + (s1[1] * s2[0])

            values.append(s3)

    final = values.pop()
    
    sq = final[0] * final[1]
    
    final[0] = pow(final[0], 2)
    final[1] = pow(final[1], 2)

    ans = [final[0], final[1], sq, sq]

    total = sum(ans)

    print(div(ans[0], total), div(ans[1], total), div(ans[2], total), div(ans[3], total))
