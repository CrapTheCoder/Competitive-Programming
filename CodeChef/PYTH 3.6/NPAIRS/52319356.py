for _ in range(int(input())):
    n = int(input())
    s = input()

    c = 0

    for i in range(n):
        for j in range(i+1, i+11):
            if j >= n:
                break

            if abs(int(s[j]) - int(s[i])) == j - i:
                c += 1

    print(c)