fibo = [0, 1]

while fibo[-1] < 10 ** 18:
    fibo.append(fibo[-1] + fibo[-2])

for i in range(int(input())):
    n = int(input())
    c = int(input())

    s = 0

    for i in fibo:
        if i > n:
            break

        s += 1

    print(c * (s - 2))