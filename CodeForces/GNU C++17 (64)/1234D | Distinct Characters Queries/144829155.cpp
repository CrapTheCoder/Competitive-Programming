#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
// #define if (false) assert
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
class SegTree {
    int n;
    vector<int> tree;
 
    void build(int i, int l, int r, const vector<int> &a) {
        if (l == r) {
            tree[i] = a[l];
            return;
        }
 
        int m = (l + r) / 2;
        int lc = i+1, rc = 2 * (m - l + 1) + i;
 
        build(lc, l, m, a);
        build(rc, m+1, r, a);
 
        tree[i] = unite(tree[lc], tree[rc]);
    }
 
    int unite(int a, int b) {
        return a | b;
    }
 
    void update(int i, int l, int r, int k, int v) {
        if (l == r) {
            tree[i] = v;
            return;
        }
 
        int m = (l + r) / 2;
        int lc = i+1, rc = 2 * (m-l+1) + i;
 
        if (k <= m)
            update(lc, l, m, k, v);
        else
            update(rc, m+1, r, k, v);
 
        tree[i] = unite(tree[lc], tree[rc]);
    }
 
    int query(int i, int l, int r, int a, int b) {
        if (a <= l && r <= b)
            return tree[i];
        
        int m = (l + r) / 2;
        int lc = i+1, rc = 2 * (m-l+1) + i;
 
        if (b <= m)
            return query(lc, l, m, a, b);
 
        if (m < a)
            return query(rc, m+1, r, a, b);
        
        return unite(query(lc, l, m, a, b), query(rc, m+1, r, a, b));
    }
 
    public:
    SegTree(const vector<int> &a) : n(a.size()), tree(2 * a.size()) {
        build(0, 0, n-1, a);
    }
 
    void update(int k, int v) {
        update(0, 0, n-1, k, v);
    }
 
    int query(int a, int b) {
        return query(0, 0, n-1, a, b);
    }
};
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    string s; cin >> s;
 
    vector<int> a;
    for (auto i : s)
        a.push_back(1 << (i - 'a'));
 
    SegTree seg(a);
 
    int q; cin >> q;
    while (q--) {
        int typ; cin >> typ;
 
        if (typ == 1) {
            int pos; char c;
            cin >> pos >> c; pos--;
            seg.update(pos, 1 << (c - 'a'));
 
        } else {
            int a, b; cin >> a >> b;
            a--; b--;
            cout << __builtin_popcount(seg.query(a, b)) << endl;
        }
    }
}