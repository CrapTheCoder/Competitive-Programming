#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX
#define MOD 1000000007

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    double dp[n+1] = {0};
    dp[0] = 1;

    for (int i = 0; i < n; i++) {
        double x; cin >> x;
        for (int j = i+1; j >= 0; j--)
            dp[j] = (j == 0 ? 0 : dp[j-1] * x) + dp[j] * (1-x);
    }

    double ans = 0;
    for (int i = 0; i <= n; i++)
        if (i > n-i)
            ans += dp[i];

    cout << setprecision(10) << ans << endl;
}
