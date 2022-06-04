def binarySearch(arr, low, high, x):
    if low > high:
        return -1

    if x >= arr[high]:
        return high

    mid = (low + high) // 2

    if arr[mid] == x:
        return mid

    if mid > 0 and arr[mid - 1] <= x < arr[mid]:
        return mid - 1

    if x < arr[mid]:
        return binarySearch(arr, low, mid - 1, x)

    return binarySearch(arr, mid + 1, high, x)

for _ in range(int(input())):
    n = int(input())
    a = sorted(set(map(int, input().split())))

    print(n - binarySearch(a, 0, len(a) - 1, n) - 1)