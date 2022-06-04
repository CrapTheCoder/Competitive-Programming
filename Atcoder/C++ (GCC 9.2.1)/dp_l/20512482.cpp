#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX
#define MOD 1000000007

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];

    int dp[n][n];

    for (int i = n-1; i >= 0; i--) {
        for (int j = i; j < n; j++) {
            if (i == j)
                dp[i][j] = a[i];
            else
                dp[i][j] = max(a[i] - dp[i+1][j], a[j] - dp[i][j-1]);
        }
    }

    cout << dp[0][n-1] << endl;
}
