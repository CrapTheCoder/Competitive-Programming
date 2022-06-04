#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX
#define MOD 1000000007

int n;
int a[3013];
int dp[3013][3013];
bool vis[3013][3013];

int solve(int i, int j) {
    if (i > j)
        return 0;

    if (vis[i][j])
        return dp[i][j];

    vis[i][j] = true;

    if (((i % 2) + (n - j - 1) % 2) % 2 == 0)
        return dp[i][j] = max(solve(i+1, j) + a[i], solve(i, j-1) + a[j]);

    return dp[i][j] = min(solve(i+1, j) - a[i], solve(i, j-1) - a[j]);
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> a[i];

    cout << solve(0, n-1) << endl;
}
