for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    lis = []

    for i in range(n - (m - 1)):
        lis.append(sum(arr[i:i + m]))

    print(max(lis))