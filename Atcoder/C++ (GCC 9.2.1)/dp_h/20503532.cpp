#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX
#define MOD 1000000007

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m; cin >> n >> m;
    char a[n][m];

    int dp[n][m];
    dp[0][0] = 1;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> a[i][j];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i == 0 && j == 0)
                continue;

            dp[i][j] = 0;

            if (a[i][j] == '.') {
                if (i-1 >= 0) dp[i][j] += dp[i-1][j];
                if (j-1 >= 0) dp[i][j] += dp[i][j-1];
            }

            dp[i][j] %= MOD;
        }
    }

    cout << dp[n-1][m-1] << endl;
}
