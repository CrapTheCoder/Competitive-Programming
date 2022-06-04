for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = [sum(list(map(int, str(a[i] * a[j])))) for i in range(n) for j in range(i+1, n)]

    print(max(b))