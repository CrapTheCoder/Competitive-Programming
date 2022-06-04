for _ in range(int(input())):
    n = int(input())
    s = input()

    c = 0
    for i in range(n // 2):
        if s[i] != s[n-i-1]:
            c += 1

    print((c+1) // 2)