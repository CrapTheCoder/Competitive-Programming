from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n, m, x, y = map(int, input().split())

    for i in range(n+1):
        flag = False

        for j in range(m+1):
            x1 = (i*x) + (j*y)
            x2 = ((n-i)*x) + ((m-j)*y)

            if x1 == x2:
                print('YES')
                flag = True
                break

            if x1 > x2:
                break

        if flag:
            break
    else:
        print('NO')
