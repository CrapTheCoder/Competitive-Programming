a = [0] * 105

for _ in range(int(input())):
    n = int(input())
    a[1 : n+1]  = list(map(int , input().split()))
    c = 0

    for i in range(1 , n+1):
        if a[a[i]] != i:
            c += 1

    print(c)