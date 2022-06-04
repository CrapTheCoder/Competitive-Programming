for _ in range(int(input())):
    lis  = []
    n = int(input())
    arr = list(map(int, input().split())) + [0]

    for i in range(n):
        if all(j < arr[i] for j in arr[i + 1:]):
            lis.append(arr[i])

    print(' '.join(str(i) for i in lis[::-1]))