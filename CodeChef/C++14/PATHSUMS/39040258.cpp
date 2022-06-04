#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int n;
vector<int> g[113];
int color[113];

void dfs(int u=0, int p=-1, int i=1) {
    color[u] = i;

    for (auto v : g[u])
        if (v != p)
            dfs(v, u, (i == 1 ? 2 : 1));
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        cin >> n;

        for (int i = 0; i < n-1; i++) {
            int u, v;
            cin >> u >> v;
            u--; v--;

            g[u].push_back(v);
            g[v].push_back(u);
        }

        dfs();

        for (int i = 0; i < n; i++)
            cout << color[i] << " ";
        cout << endl;

        for (int i = 0; i <= n; i++)
            g[i].clear();
    }
}
