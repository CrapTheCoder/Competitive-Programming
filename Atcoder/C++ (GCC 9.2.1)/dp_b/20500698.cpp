#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, k; cin >> n >> k;

    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int dp[n];
    fill(dp, dp+n, INF); dp[0] = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= k; j++)
            if (i-j >= 0)
                dp[i] = min(dp[i], dp[i-j] + abs(a[i] - a[i-j]));
    }

    cout << dp[n-1] << endl;
}
