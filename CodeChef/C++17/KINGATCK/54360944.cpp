#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int n, m;
bool vis[200013];
vector<int> g[200013];
int edges = 0, counter = 0;

void dfs(int u) {
    if (vis[u]) return;
    vis[u] = true;

    counter++;
    for (auto v : g[u]) {
        edges++; dfs(v);
    }
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
    
    int tc; cin >> tc;
    while (tc--) {
        cin >> n >> m;
        
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v; u--; v--;

            g[u].push_back(v);
            g[v].push_back(u);
        }

        int total = 0, comps = 0;
        for (int u = 0; u < n; u++) {
            if (!vis[u]) {
                dfs(u); comps++;
                if (edges / 2 == counter * (counter - 1) / 2)
                    total++;
                
                edges = counter = 0;
            }
        }

        if (comps == 1)
            cout << 0 << endl;
        else
            cout << total << endl;

        fill(vis, vis+n, false);
        for (int i = 0; i < n; i++)
            g[i].clear();
    }
}
