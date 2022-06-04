for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(sum((a[i] & a[j]) == a[i] for i in range(n) for j in range(i+1, n)))
