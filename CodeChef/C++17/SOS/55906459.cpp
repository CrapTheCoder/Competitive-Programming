#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) (iter).size();

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int n;
string s;
vector<int> tree[200013];

bool dfs(int u, vector<pair<int, int>> &k, int p=-1) {
    vector<pair<int, int>> h;
    for (auto v : tree[u])
        if (v != p && !dfs(v, h, u))
            return false;

    if (s[u] == 'B') {
        for (auto [xr, xg] : h)
            if (xr == 0 || xg == 0)
                return false;

        k.push_back({0, 0});
        return true;
    }

    int cr = 0, cg = 0;
    for (auto [xr, xg] : h) {
        xr += (int) (s[u] == 'R');
        xg += (int) (s[u] == 'G');

        if (xr == 0) cr++;
        if (xg == 0) cg++;
        
        k.push_back({xr, xg});
    }

    if (h.size() >= 2 && (cr > 1 || cg > 1))
        return false;
    
    return true;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        cin >> n >> s;
        for (int i = 0; i < n; i++)
            tree[i].clear();
        
        for (int i = 0; i < n-1; i++) {
            int u, v; cin >> u >> v;
            u--; v--;
            tree[u].push_back(v);
            tree[v].push_back(u);
        }

        vector<pair<int, int>> k;
        cout << (dfs(0, k) ? "Yes" : "No") << endl;
    }
}
