for _ in range(int(input())):
    n = int(input())
    mini = float('inf')

    for i in range(int(n ** 0.5), 0, -1):
        if n % i == 0 and i != n // i:
            if i + n // i < mini:
                mini = i + n // i

    print(mini)
