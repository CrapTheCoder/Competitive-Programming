#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

#define int long long
#define MOD 1000000007
#define MAXN 1000013

int c1[MAXN], c2[MAXN];
int dp0[MAXN], dp1[MAXN], dp2[MAXN];

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    c1[0] = 1;
    c2[0] = c2[2] = 1;
    dp0[0] = dp0[1] = dp0[2] = 1;

    for (int i = 3; i < MAXN; i++) {
        c1[i] = i%3 == 0 ? 1 : 0;
        c2[i] = (c2[i-2] + c2[i-3]) % MOD;

        dp0[i] = dp0[i-1] + dp0[i-3] + 2 * dp2[i-2];
        dp1[i] = dp0[i-3] + dp1[i-3];
        dp2[i] = dp1[i-1] + dp2[i-3];

        dp0[i] %= MOD;
        dp1[i] %= MOD;
        dp2[i] %= MOD;
    }

    int t; cin >> t;
    while (t--) {
        int k, n; cin >> k >> n;

        if (k == 1) cout << c1[n];
        else if (k == 2) cout << c2[n];
        else cout << dp0[n];

        cout << endl;
    }
}
