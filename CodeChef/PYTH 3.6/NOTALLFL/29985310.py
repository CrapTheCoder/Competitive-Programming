t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = [0] * (k + 1)
    k -= 1
    lk = 0
    hl = 0
    now = 0
    no = 0
    for i in range(n):
        count[a[i]] += 1
        if count[a[i]] == 1:
            now += 1
        while now > k:
            count[a[no]] -= 1
            if count[a[no]] == 0:
                now -= 1
            no += 1
        if i - no + 1 >= hl - lk + 1:
            hl = i
            lk = no

    print((hl + 1) - lk)