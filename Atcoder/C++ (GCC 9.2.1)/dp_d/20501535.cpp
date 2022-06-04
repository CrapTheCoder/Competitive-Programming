#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, w; cin >> n >> w;
    int wa[n+1], va[n+1];

    for (int i = 1; i <= n; i++)
        cin >> wa[i] >> va[i];

    int dp[n+1][w+1];
    for (int i = 0; i <= n; i++)
        for (int j = 0; j < w+1; j++)
            dp[i][j] = 0;

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= w; j++) {
            dp[i][j] = dp[i-1][j];
            if (j - wa[i] >= 0)
                dp[i][j] = max(dp[i][j], dp[i-1][j - wa[i]] + va[i]);
        }
    }

    cout << dp[n][w] << endl;
}
