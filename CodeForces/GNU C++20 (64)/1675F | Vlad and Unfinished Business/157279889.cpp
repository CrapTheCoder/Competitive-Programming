#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
int n, k;
int x, y;
bool marked[200013];
vector<int> tree[200013];
 
unordered_set<int> path;
 
int total = 0;
bool dfs(int u, int p=-1) {
    if (path.contains(u) && p != -1)
        return false;
 
    bool ret = marked[u];
    for (auto v: tree[u])
        if (v != p && dfs(v, u))
            total += 2, ret = true;
 
    return ret;
}
 
// Finds path between x and y with standard backtracking
bool path_xy(int u=x, int p=-1) {
    path.insert(u);
    if (u == y)
        return true;
 
    for (auto v: tree[u])
        if (v != p)
            if (path_xy(v, u))
                return true;
 
    path.erase(u);
    return false;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        cin >> n >> k;
 
        // Cleanup
        path.clear(); total = 0;
        for (int i = 0; i <= n; i++)
            tree[i].clear(), marked[i] = false;
 
        // Input (0-based)
        cin >> x >> y; x--; y--;
        for (int i = 0; i < k; i++) {
            int cur; cin >> cur; cur--;
            marked[cur] = true;
        }
 
        for (int i = 0; i < n-1; i++) {
            int u, v; cin >> u >> v; u--; v--;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }
 
        // For each node in path, find minimum distance for the tasks from that node
        int ans = 0; path_xy();
        for (auto u : path) {
            dfs(u, -1);
            ans += total;
            total = 0;
        }
 
        ans += path.size() - 1;
        cout << ans << endl;
    }
}