for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mini = float('inf')
    maxi = float('-inf')

    for current in range(n):
        count = 1  # Count is initially 1 because you have to include the current index too

        # After the current index
        for after in range(current+1, n):
            if a[after] - a[after-1] > 2:
                break

            count += 1

        # Before the current index
        for before in range(current-1, -1, -1):
            if a[before+1] - a[before] > 2:
                break

            count += 1
            
        mini = min(mini, count)
        maxi = max(maxi, count)

    print(mini, maxi)