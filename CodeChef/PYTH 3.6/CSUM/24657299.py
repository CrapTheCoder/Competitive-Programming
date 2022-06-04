def sol():
    # Create an empty hash set
    s = set()

    for i in range(n):
        temp = k - a[i]

        if temp in s:
            return 'Yes'

        s.add(a[i])

    return 'No'

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(sol())