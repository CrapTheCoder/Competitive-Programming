#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    int a[n][3];
    for (int i = 0; i < n; i++)
        cin >> a[i][0] >> a[i][1] >> a[i][2];

    int dp[n][3];
    dp[0][0] = a[0][0];
    dp[0][1] = a[0][1];
    dp[0][2] = a[0][2];

    for (int i = 1; i < n; i++) {
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i][0];
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + a[i][1];
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + a[i][2];
    }

    cout << max(dp[n-1][0], max(dp[n-1][1], dp[n-1][2])) << endl;
}
