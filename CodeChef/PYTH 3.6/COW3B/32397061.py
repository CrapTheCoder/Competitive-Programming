from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = int(input())
    b = list(map(int, input().split()))
    
    x = set(b)

    i = cnt = 0

    while i < n:
        j = i

        while j < n and a[j] in x:
            j += 1

        if i != j:
            cnt += 1

        i = j + 1

    print(cnt)
