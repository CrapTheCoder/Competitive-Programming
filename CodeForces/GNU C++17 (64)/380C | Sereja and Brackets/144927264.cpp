#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
struct node {
    int to, op, cl;
};
 
class SegTree {
    int n;
    vector<node> tree;
 
    void build(int i, int l, int r, const string &s) {
        if (l == r) {
            if (s[l] == '(')
                tree[i] = {0, 1, 0};
            else
                tree[i] = {0, 0, 1};
            
            return;
        }
 
        int m = (l + r) / 2;
        int lc = i+1, rc = (m-l+1) * 2 + i;
 
        build(lc, l, m, s);
        build(rc, m+1, r, s);
 
        tree[i] = unite(tree[lc], tree[rc]);
    }
 
    node query(int i, int l, int r, int a, int b) {
        if (a <= l && r <= b)
            return tree[i];
        
        int m = (l + r) / 2;
        int lc = i+1, rc = (m-l+1) * 2 + i;
 
        if (b <= m)
            return query(lc, l, m, a, b);
 
        if (m < a)
            return query(rc, m+1, r, a, b);
 
        return unite(query(lc, l, m, a, b), query(rc, m+1, r, a, b));
    }
 
    node unite(node a, node b) {
        int ext = min(a.op, b.cl);
 
        return {a.to + b.to + ext,
                a.op + b.op - ext,
                a.cl + b.cl - ext};
    }
 
    public:
    SegTree(const string &s) : n(s.size()), tree(s.size() * 2) {
        build(0, 0, n-1, s);
    }
 
    int query(int a, int b) {
        return query(0, 0, n-1, a, b).to;
    }
};
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    string s; cin >> s;
 
    SegTree seg(s);
 
    int q; cin >> q;
    while (q--) {
        int l, r;
        cin >> l >> r; l--; r--;
 
        cout << 2 * seg.query(l, r) << endl;
    }
}