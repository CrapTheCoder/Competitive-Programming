for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    arr = sorted(arr)
    print(min([abs(j - arr[i + 1]) for i, j in enumerate(arr[:-1])]))