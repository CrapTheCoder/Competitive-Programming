#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int dp[n];
    fill(dp, dp+n, INF); dp[0] = 0;

    for (int i = 0; i < n; i++) {
        if (i - 1 >= 0) dp[i] = min(dp[i], dp[i-1] + abs(a[i] - a[i-1]));
        if (i - 2 >= 0) dp[i] = min(dp[i], dp[i-2] + abs(a[i] - a[i-2]));
    }

    cout << dp[n-1] << endl;
}
