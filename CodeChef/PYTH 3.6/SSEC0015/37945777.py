a = list(map(int, input()))
n = len(a)

maxi = -1
si, sj = -1, -1

for i in range(n):
    s = a[i]

    j = i

    for j in range(i+1, n):
        if a[j] <= a[j-1]:
            j -= 1
            break

        s += a[j]

    if maxi < s:
        maxi = s
        si, sj = i+1, j+1

print(f'{maxi}:{si}-{sj}')