def count(n, a):
    if n == 0:
        return sum(a[i-1] < a[i] > a[i+1] for i in range(1, on-1)) + sum(a[i-1] > a[i] < a[i+1] for i in range(1, on-1))

    return count(n-1, a+[0]) + count(n-1, a+[1]) + count(n-1, a+[2])

for _ in range(int(input())):
    on = int(input())
    print(count(on, []))