#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int n, k;
bool frnd[200013];
int reach[200013];
vector<int> tree[200013];
 
int dfs(int u=0, int p=-1) {
    if (frnd[u])
        return reach[u] = 0;
 
    for (auto v : tree[u])
        if (v != p)
            reach[u] = min(dfs(v, u) + 1, reach[u]);
    
    return reach[u];
}
 
int dfs2(int u=0, int p=-1, int d=0) {
    if (reach[u] - d <= 0)
        return false;
    
    if (u != 0 && tree[u].size() == 1)
        return true;
    
    for (auto v : tree[u])
        if (v != p)
            if (dfs2(v, u, d+1))
                return true;
    
    return false;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
    
    int tc; cin >> tc;
    while (tc--) {
        int n, k;
        cin >> n >> k;
 
        fill(frnd, frnd+n, false);
        fill(reach, reach+n, INF);
 
        for (int i = 0; i < k; i++) {
            int x; cin >> x; x--;
            frnd[x] = true;
        }
 
        for (int i = 0; i < n-1; i++) {
            int u, v;
            cin >> u >> v; u--; v--;
            
            tree[u].push_back(v);
            tree[v].push_back(u);
        }
 
        dfs();
 
        if (dfs2())
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
        
        for (int i = 0; i < n; i++)
            tree[i].clear();
    }
}