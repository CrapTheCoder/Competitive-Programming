import os

n, *arr = map(int, os.read(0, 9999999).split())
arr = sorted(arr, reverse=True)
print(max(price * (i + 1) for i, price in enumerate(arr)))