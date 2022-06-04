def main():
    for _ in range(int(input())):
        n, L, R = map(int, input().split())
        a = sorted(map(int, input().split()))

        c = 0

        ls = []
        rs = []

        l, r = 0, n-1

        for i in range(n-1, -1, -1):
            while l < n and (not L <= int(str(a[l]) + str(a[i]))):
                l += 1

            ls.append(l)

        for i in range(n):
            while r >= 0 and (not int(str(a[r]) + str(a[i])) <= R):
                r -= 1

            rs.append(r)

        ls.reverse()

        s = 0
        for i in range(n):
            x = rs[i] - ls[i] + 1
            if x > 0:
                s += x

        print(s)

main()