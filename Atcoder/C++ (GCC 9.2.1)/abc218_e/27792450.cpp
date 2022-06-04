#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

struct UFDS {
    int n;
    vector<int> siz, par;

    UFDS(int _n): n(_n), siz(_n), par(_n) {
        iota(par.begin(), par.end(), 0);
        fill(siz.begin(), siz.end(), 1);
    };

    int find_rep(int u) {
        if (u == par[u]) return u;
        return par[u] = find_rep(par[u]);
    }

    bool is_connected(int u, int v) {
        return find_rep(u) == find_rep(v);
    }

    bool union_sets(int u, int v) {
        u = find_rep(u);
        v = find_rep(v);

        if (u != v) {
            if (siz[u] < siz[v])
                swap(u, v);

            par[v] = u;
            siz[u] += siz[v];

            return true;
        }

        return false;
    }

    set<int> representatives() {
        return set<int>(par.begin(), par.end());
    }

    int component_size(int u) {
        return siz[find_rep(u)];
    }

    int components_count() {
        return representatives().size();
    }

    map<int, vector<int>> rep_components() {
        map<int, vector<int>> rep_children;
        for (int i = 0; i < n; i++)
            rep_children[par[i]].push_back(i);

        return rep_children;
    }
};

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<pair<int, pair<int, int>>> edges;
    
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w; u--; v--;
        edges.push_back({w, {u, v}});
    }
    
    sort(all(edges));

    UFDS ufds(n); int total = 0;
    for (auto [w, uv] : edges)
        if (!ufds.union_sets(uv.first, uv.second))
            total += max(0LL, w);
    
    cout << total << endl;
}
