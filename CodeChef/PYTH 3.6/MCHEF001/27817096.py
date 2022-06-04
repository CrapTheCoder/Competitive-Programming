from math import sqrt

def solve(n):
    c = 0
    l = [1]
    i = 2

    while i <= sqrt(n):
        if n % i == 0:
            if i == (n / i):
                c += 1
                l.append(i)
            else:
                c += 2
                l.append(i)
                l.append(n // i)

        i += 1

    return l, c

def isSubsetSum(set, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    if set[n - 1] > sum:
        return isSubsetSum(set, n - 1, sum)

    return isSubsetSum(set, n - 1, sum) or isSubsetSum(set, n - 1, sum - set[n - 1])

l = [70, 836, 4030, 5830, 7192, 7912, 9272, 10430, 10570, 10792, 10990, 11410, 11690, 12110, 12530, 12670, 13370, 13510, 13790, 13930, 14770, 15610, 15890, 16030, 16310, 16730, 16870, 17272, 17570, 17990, 18410, 18830, 18970, 19390, 19670, 19810]

for _ in range(int(input())):
    n = int(input())
    a, c = solve(n)

    if n in l:
        print('SPECIAL')
    else:
        if sum(a) > n and not isSubsetSum(a, c, n):
            print('SPECIAL')
        else:
            print('NOT SPECIAL')
