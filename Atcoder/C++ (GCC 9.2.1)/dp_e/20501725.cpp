#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

signed main() {
    // ios::sync_with_stdio(false); cin.tie(NULL);

    int n, w, v=0; cin >> n >> w;
    int wa[n+1], va[n+1];

    for (int i = 1; i <= n; i++) {
        cin >> wa[i] >> va[i];
        v += va[i];
    }

    int dp[n+1][v+1];
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= v; j++)
                dp[i][j] = INF;

    dp[0][0] = 0;

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= v; j++) {
            dp[i][j] = dp[i-1][j];
            if (j - va[i] >= 0)
                dp[i][j] = min(dp[i][j], dp[i-1][j - va[i]] + wa[i]);
        }
    }

    int maxi = 0;
    for (int j = 0; j <= v; j++) {
        if (dp[n][j] <= w)
            maxi = j;
    }

    cout << maxi << endl;
}
