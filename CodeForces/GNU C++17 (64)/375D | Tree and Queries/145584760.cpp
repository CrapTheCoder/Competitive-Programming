#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
const int BLOCK = 200;
 
struct query {
    int l, r, k, i;
};
 
struct range {
    int l, r;
};
 
class Mo {
    int n;
    vector<int> a;
    vector<query> qs;
 
    int block(int i) {
        return i / BLOCK;
    }
 
public:
    Mo(const vector<int> &_a, const vector<query> &_qs) : n(_a.size()), a(_a), qs(_qs) {
        sort(qs.begin(), qs.end(), [&](query x, query y) {
            if (block(x.l) != block(y.l))
                return block(x.l) < block(y.l);
 
            return (block(x.l) & 1) ? (block(x.r) > block(y.r)) : (block(x.r) < block(y.r));
        });
    }
 
    void process() {
        int l = 0, r = -1;
        unordered_map<int, int> fq, tfq;
 
        auto add = [&](int i) { fq[a[i]]++; tfq[fq[a[i]]]++; };
        auto rem = [&](int i) { tfq[fq[a[i]]]--; fq[a[i]]--; };
 
        vector<int> ans(qs.size());
        for (auto [ql, qr, k, i] : qs) {
            while (r < qr) add(++r);
            while (l > ql) add(--l);
            while (r > qr) rem(r--);
            while (l < ql) rem(l++);
            ans[i] = tfq[k];
        }
 
        for (auto i : ans)
            cout << i << endl;
    }
};
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, m;
    cin >> n >> m;
 
    int c[n];
    for (int i = 0; i < n; i++)
        cin >> c[i];
 
    vector<int> tree[n];
    for (int i = 0; i < n-1; i++) {
        int u, v; cin >> u >> v;
        u--; v--;
 
        tree[u].push_back(v);
        tree[v].push_back(u);
    }
 
    vector<int> a(n);
    vector<range> st(n);
 
    int cur = 0;
    function<void(int, int)> dfs = [&](int u, int p) {
        st[u].l = cur++;
        a[st[u].l] = c[u];
 
        for (auto v : tree[u])
            if (v != p)
                dfs(v, u);
 
        st[u].r = cur-1;
    };
 
    dfs(0, -1);
 
    vector<query> qs(m);
    for (int i = 0; i < m; i++) {
        int v; cin >> v; v--;
        qs[i].l = st[v].l, qs[i].r = st[v].r;
        cin >> qs[i].k; qs[i].i = i;
    }
 
    Mo mo(a, qs);
    mo.process();
}