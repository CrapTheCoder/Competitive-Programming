for _ in range(int(input())):
    n = int(input())
    m = list(input())
    q = int(input())

    for __ in range(q):
        i, d = input().split()

        m[int(i)] = d

        if m == m[::-1]:
            print('Palindrome')
        else:
            print(-1)
