#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF LLONG_MAX >> 1
#define MOD 1000000007

signed main() {
    // ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;
    int dp[n][n];

    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int pre[n+1]; pre[0] = 0;
    for (int i = 0; i < n; i++)
        pre[i+1] = pre[i] + a[i];

    for (int i = n-1; i >= 0; i--) {
        dp[i][i] = 0;

        for (int j = i+1; j < n; j++) {
            dp[i][j] = INF;
            for (int k = i; k < j; k++)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + (pre[j+1] - pre[i]));
        }
    }

    cout << dp[0][n-1] << endl;
}
