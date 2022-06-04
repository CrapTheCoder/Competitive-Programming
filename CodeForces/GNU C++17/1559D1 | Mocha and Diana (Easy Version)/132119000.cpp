#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
struct UFDS {
    int n;
    vector<int> siz, par;
 
    UFDS(int _n): n(_n), siz(_n), par(_n) {
        iota(par.begin(), par.end(), 0);
        fill(siz.begin(), siz.end(), 1);
    };
 
    int find_rep(int u) {
        if (u == par[u])
            return u;
 
        return par[u] = find_rep(par[u]);
    }
 
    bool connected(int u, int v) {
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
 
    int n, m1, m2;
    cin >> n >> m1 >> m2;
 
    UFDS g1(n), g2(n);
 
    for (int i = 0; i < m1; i++) {
        int u, v; cin >> u >> v;
        u--; v--;
 
        g1.union_sets(u, v);
    }
 
    for (int i = 0; i < m2; i++) {
        int u, v; cin >> u >> v;
        u--; v--;
 
        g2.union_sets(u, v);
    }
 
    vector<pair<int, int>> add;
    for (int u = 0; u < n; u++) {
        for (int v = 0; v < u; v++) {
            if (!g1.connected(u, v) && !g2.connected(u, v)) {
                g1.union_sets(u, v);
                g2.union_sets(u, v);
                add.push_back({v+1, u+1});
            }
        }
    }
 
    cout << add.size() << endl;
    for (auto [x, y] : add)
        cout << x << " " << y << endl;
}