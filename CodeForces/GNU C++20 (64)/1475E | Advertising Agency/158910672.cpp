#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int power(int x, int y, int mod=0) {
    if (mod)
        x %= MOD;
 
    int z = 1;
    while (y) {
        if (y & 1)
            z = mod ? (z*x) % mod : (z*x);
 
        x = mod ? (x*x) % mod : (x*x);
        y >>= 1;
    }
 
    return z;
}
 
int inverse(int d) {
    return power(d, MOD-2, MOD);
}
 
const int MAX = 1013;
int f[MAX];
 
int ncr(int n, int r) {
    return f[n] * inverse(f[r] * f[n-r]) % MOD;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    f[0] = 1;
    for (int i = 1; i < MAX; i++)
        f[i] = f[i-1] * i % MOD;
 
    int tc; cin >> tc;
    while (tc--) {
        int n, k; cin >> n >> k;
 
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
 
        sort(a, a+n);
 
        int cur, i;
        for (i = n-1; i >= n-k; i--) {
            if (i+1 == n || a[i] != a[i+1])
                cur = 0;
 
            cur++;
        }
 
        cout << ncr(count(a, a+n, a[i+1]), cur) << endl;
    }
}