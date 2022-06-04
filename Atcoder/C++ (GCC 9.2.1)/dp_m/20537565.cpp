#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX
#define MOD 1000000007

signed main() {
    // ios::sync_with_stdio(false); cin.tie(NULL);

    int n, k; cin >> n >> k;
    int dp[k+1] = {0};
    dp[0] = 1;

    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        int f[k+5] = {0};

        for (int j = k; j >= 0; j--) {
            int l = j+1;
            int r = min(x+j, k);

            f[l] += dp[j];
            f[r+1] -= dp[j];
        }

        for (int i = 1; i <= k; i++)
            f[i] += f[i-1];

        for (int i = 0; i <= k; i++)
            dp[i] = (dp[i] + f[i]) % MOD;
    }

    cout << dp[k] << endl;
}
