#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    string s; cin >> s; int n = s.size();
    string t; cin >> t; int m = t.size();

    int dp[n+1][m+1];
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++)
            dp[i][j] = 0;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            if (s[i-1] == t[j-1])
                dp[i][j] = dp[i-1][j-1] + 1;
        }
    }

    string ans;

    int i = n, j = m;
    while (i > 0 && j > 0) {
        if (s[i-1] == t[j-1]) ans += s[i-1], i--, j--;
        else if (dp[i][j] == dp[i-1][j]) i--;
        else if (dp[i][j] == dp[i][j-1]) j--;
    }

    reverse(ans.begin(), ans.end());
    cout << ans << endl;
}
