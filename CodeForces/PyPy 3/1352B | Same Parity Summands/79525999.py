for _ in range(int(input())):
    n, k = map(int, input().split())
 
    if n % 2 == 1:
        answer = [1] * (k-1)
 
        if sum(answer) >= n or (n - sum(answer)) % 2 == 0:
            print('NO')
 
        else:
            print('YES')
            print(*answer + [n - sum(answer)])
 
    else:
        answer = [1] * (k - 1)
 
        if sum(answer) >= n or (n - sum(answer)) % 2 == 0:
            answer = [2] * (k - 1)
 
            if sum(answer) >= n:
                print('NO')
            else:
                print('YES')
                print(*answer + [n - sum(answer)])
 
        else:
            print('YES')
            print(*answer + [n - sum(answer)])