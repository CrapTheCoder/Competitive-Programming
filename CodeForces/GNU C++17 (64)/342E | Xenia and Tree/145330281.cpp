#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int INF = LLONG_MAX >> 1;
const int LOG = 20;
const int BLOCK = 300;
 
int n, m;
int md[100013];
vector<int> reds;
vector<int> tree[100013];
 
void count() {
    bool vis[n]; memset(vis, false, sizeof vis);
    queue<pair<int, int>> q;
 
    for (auto u : reds)
        q.push({u, 0});
 
    while (!q.empty()) {
        auto [u, w] = q.front(); q.pop();
 
        if (!vis[u]) {
            vis[u] = true, md[u] = min(md[u], w);
            for (auto v : tree[u])
                q.push({v, w+1});
        }
    }
}
 
int dep[100013];
int par[100013][LOG];
 
void dfs(int u=0, int p=0, int d=0) {
    par[u][0] = p; dep[u] = d;
    for (int j = 1; j < LOG; j++)
        par[u][j] = par[par[u][j-1]][j-1];
 
    for (auto v : tree[u])
        if (v != p)
            dfs(v, u, d+1);
}
 
int dist(int u, int v) {
    int ans = 0;
    if (dep[u] < dep[v])
        swap(u, v);
 
    int k = dep[u] - dep[v];
 
    for (int i = 0; i < LOG; i++) {
        if ((k >> i) & 1) {
            u = par[u][i];
            ans += 1 << i;
        }
    }
 
    if (u == v)
        return ans;
 
    for (int i = LOG - 1; i >= 0; i--) {
        if (par[u][i] != par[v][i]) {
            u = par[u][i], v = par[v][i];
            ans += 2 * (1 << i);
        }
    }
 
    return ans+2;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    cin >> n >> m;
 
    for (int i = 0; i < n-1; i++) {
        int u, v; cin >> u >> v;
        u--; v--;
 
        tree[u].push_back(v);
        tree[v].push_back(u);
    }
 
    dfs();
    reds.push_back(0);
    fill(md, md+n, INF);
 
    while (m--) {
        int t, v;
        cin >> t >> v; v--;
 
        if (t == 1) {
            reds.push_back(v);
            if (reds.size() >= BLOCK)
                count(), reds.clear();
 
        } else {
            int mini = md[v];
            for (auto u : reds)
                mini = min(mini, dist(u, v));
 
            cout << mini << endl;
        }
    }
}