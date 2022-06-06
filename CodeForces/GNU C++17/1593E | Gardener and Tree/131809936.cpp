#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n, k; cin >> n >> k;
        vector<int> g[n];
        int deg[n] = {0};
 
        for (int i = 0; i < n-1; i++) {
            int u, v; cin >> u >> v;
            u--; v--;
 
            g[u].push_back(v); deg[u]++;
            g[v].push_back(u); deg[v]++;
        }
 
        queue<pair<int, int>> lf;
        for (int i = 0; i < n; i++)
            if (deg[i] <= 1)
                lf.push({i, k});
 
        bool vis[n] = {false};
 
        while (!lf.empty()) {
            auto cuk = lf.front(); lf.pop();
            int u = cuk.first, ck = cuk.second;
 
            if (ck == 0)
                continue;
 
            if (vis[u]) continue;
            vis[u] = true;
 
            for (auto v : g[u]) {
                deg[v]--;
                if (deg[v] <= 1)
                    lf.push({v, ck-1});
            }
        }
 
        int cnt = 0;
        for (int i = 0; i < n; i++)
            if (!vis[i])
                cnt++;
 
        cout << cnt << endl;
    }
}