#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

#define MOD 1000000007
#define MAXN 1000013

int c1[MAXN];
int c2[MAXN];
int dp[MAXN * 72];

int hasher(int a, int b, int c) {
    int base = min({a, b, c});
    a -= base; b -= base; c -= base;
    return base * 67 + a + b * 4 + c * 16;
}

int solve(int a, int b, int c) {
    if (a < 0 || b < 0 || c < 0)
        return 0;

    int abc[3] = {a, b, c}; sort(abc, abc+3);
    c = abc[0]; b = abc[1]; a = abc[2];

    int h = hasher(a, b, c);
    if (dp[h] >= 0)
        return dp[h];

    long long s = solve(a-3, b, c);
    if (a == b && b == c)
        s += solve(a-1, b-1, c-1);

    if (a == b)
        s += solve(a-2, b-2, c);

    return dp[h] = s % MOD;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    c1[0] = 1;
    c2[0] = c2[2] = 1;

    fill(dp, dp + (MAXN * 72), -1);
    dp[hasher(0, 0, 0)] = 1;

    for (int i = 3; i < MAXN; i++) {
        c1[i] = i%3 == 0 ? 1 : 0;
        c2[i] = (c2[i-2] + c2[i-3]) % MOD;
    }

    int t; cin >> t;
    while (t--) {
        int k, n; cin >> k >> n;

        if (k == 1) cout << c1[n];
        else if (k == 2) cout << c2[n];
        else cout << solve(n, n, n);

        cout << endl;
    }
}
