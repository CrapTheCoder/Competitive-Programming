#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

int n, m;
int dp[100013];

vector<int> par[100013];

int solve(int u) {
    if (dp[u] != -1)
        return dp[u];

    dp[u] = 0;
    for (auto i : par[u])
        dp[u] = max(dp[u], solve(i) + 1);

    return dp[u];
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n >> m;
    fill(dp, dp+n, -1);

    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        u--; v--;

        par[v].push_back(u);
    }

    for (int u = 0; u < n; u++)
        solve(u);

    cout << *max_element(dp, dp+n) << endl;
}
