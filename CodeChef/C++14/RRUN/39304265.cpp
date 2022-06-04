#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define MOD 1000000007

int expo(int x, int y) {
    x %= MOD;
    int z = 1;

    while (y) {
        if (y & 1)
            z = (z*x) % MOD;

        x = (x*x) % MOD;
        y >>= 1;
    }

    return z;
}

int f[1000005];

int ncr(int x, int y) {
    return (f[x] * expo(f[y] * f[x-y], MOD-2)) % MOD;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    f[0] = 1;
    for (int i = 1; i < 1000005; i++)
        f[i] = (f[i-1] * i) % MOD;

    int t; cin >> t;

    while (t--) {
        int n; cin >> n;

        pair<int, int> a[n];

        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            a[i] = {x, i};
        }

        sort(a, a+n);

        int l[n];

        for (int i = 0; i < n; i++) {
            int s = 1;
            if (n-i-1 >= 1) s = (s + ncr(n-i-1, 1)) % MOD;
            if (n-i-1 >= 2) s = (s + ncr(n-i-1, 2)) % MOD;

            l[a[i].second] = (expo(2, i) * s - 1) % MOD;

            if (l[a[i].second] < 0)
                l[a[i].second] += MOD;
        }

        for (int i = 0; i < n; i++)
            cout << l[i] << " ";
        cout << endl;
    }
}
