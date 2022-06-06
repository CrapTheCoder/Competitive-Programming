#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) (iter).size();
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
struct UFDS {
    int n;
    vector<int> siz, par, val;
    set<int> maxi;
 
    UFDS(int _n): n(_n), siz(_n), par(_n), val(_n) {
        iota(par.begin(), par.end(), 0);
        fill(siz.begin(), siz.end(), 1);
        fill(val.begin(), val.end(), -1);
        maxi.insert(0);
    };
 
    int find_rep(int u) {
        if (u == par[u]) return u;
        return par[u] = find_rep(par[u]);
    }
 
    bool is_connected(int u, int v) {
        return find_rep(u) == find_rep(v);
    }
 
    int union_sets(int u, int v) {
        u = find_rep(u);
        v = find_rep(v);
 
        if (u != v) {
            if (siz[u] < siz[v])
                swap(u, v);
 
            par[v] = u;
            siz[u] += siz[v];
            val[u] += val[v];
            maxi.insert(val[u]);
 
            return u;
        }
 
        return -1;
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
 
    int n; cin >> n;
    
    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    
    int b[n];
    for (int i = 0; i < n; i++) {
        cin >> b[i]; b[i]--;
    }
    
    UFDS ufds(n);
 
    int res[n] = {};
    for (int r = n-1; r >= 0; r--) {
        int i = b[r];
 
        res[r] = *ufds.maxi.rbegin();
 
        ufds.val[i] = a[i];
        ufds.maxi.insert(a[i]);
        
        if (i-1 >= 0 && ufds.val[i-1] != -1) ufds.union_sets(i, i-1);
        if (i+1 < n && ufds.val[i+1] != -1) ufds.union_sets(i, i+1);
    }
 
    for (int i = 0; i < n; i++)
        cout << res[i] << endl;
}