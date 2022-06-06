def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
 
def lcm(a, b):
    return (a * b) / gcd(a, b)
 
 
mod = int(1e9) + 7
 
 
def power(k, n):
    if n == 0:
        return 1
    if n % 2:
        return (power(k, n - 1) * k) % mod
    t = power(k, n // 2)
    return (t * t) % mod
 
 
def totalPrimeFactors(n):
    count = 0
    if (n % 2) == 0:
        count += 1
        while (n % 2) == 0:
            n //= 2
 
    i = 3
    while i * i <= n:
        if (n % i) == 0:
            count += 1
            while (n % i) == 0:
                n //= i
        i += 2
    if n > 2:
        count += 1
    return count
 
 
# #MAXN = int(1e7 + 1)
# # spf = [0 for i in range(MAXN)]
#
#
# def sieve():
#     spf[1] = 1
#     for i in range(2, MAXN):
#         spf[i] = i
#     for i in range(4, MAXN, 2):
#         spf[i] = 2
#
#     for i in range(3, mt.ceil(mt.sqrt(MAXN))):
#         if (spf[i] == i):
#             for j in range(i * i, MAXN, i):
#                 if (spf[j] == j):
#                     spf[j] = i
#
#
# def getFactorization(x):
#     ret = 0
#     while (x != 1):
#         k = spf[x]
#         ret += 1
#         # ret.add(spf[x])
#         while x % k == 0:
#             x //= k
#
#     return ret
 
 
# Driver code
 
# precalculating Smallest Prime Factor
# sieve()
 
def getdiffpow2(x):
    t = 1
    while t < x:
        t *= 2
    return t - x
 
 
def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = [0 for i in range(max(a) + 1)]
        for i in a:
            cnt[i] += 1
        for i in range(1, max(a) + 1):
            cnt[i] += cnt[i - 1]
        last = max(a)
        ans = float('inf')
        i = 1
        j = 1
        k = 1
        while i < 2 * n:
            j=1
            while j < 2 * n:
                k=1
                while k < 2 * n:
                    #print(i, j, k)
                    if i + j + k >= n:
                        now = 0
                        l = 0
                        r = last
                        ind = last
                        while l <= r:
                            mid = (l + r) // 2
                            if cnt[mid] <= i:
                                ind = mid
                                l = mid + 1
                            else:
                                r = mid - 1
                        now += i - cnt[ind]
                        ind2 = -1
                        l = ind + 1
                        r = last
                        while l <= r:
                            mid = (l + r) // 2
                            if cnt[mid] - cnt[ind] <= j:
                                ind2 = mid
                                l = mid + 1
                            else:
                                r = mid - 1
                        if ind2==-1:
                            if k>=(cnt[last]-cnt[ind]):
                                now+=j
                                now+=(k-(cnt[last]-cnt[ind]))
                            else:
                                now=float('inf')
                        else:
                            now += (j - (cnt[ind2] - cnt[ind]))
                            if k>=(cnt[last] - cnt[ind2]):
                                now += (k - (cnt[last] - cnt[ind2]))
                            else:
                                now=float('inf')
                        #print(i, j, k, ind, cnt[ind], ind2, cnt[ind2], now)
                        ans = min(ans, now)
                    k *= 2
                j *= 2
            i *= 2
        print(ans)
 
        # = map(int,input().split())
        # s=input()
 
    return
 
 
if __name__ == "__main__":
    main()