#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
class SegTree {
    int n;
    vector<int> tree;
 
    void update(int i, int l, int r, int pos, int v) {
        if (l == r) {
            tree[i] = v;
            return;
        }
 
        int m = (l + r) >> 1;
        int lc = i+1, rc = 2 * (m-l+1) + i;
 
        if (pos <= m)
            update(lc, l, m, pos, v);
        else
            update(rc, m+1, r, pos, v);
 
        tree[i] = unite(tree[lc], tree[rc]);
    }
 
    int query(int i, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr)
            return tree[i];
 
        int m = (l + r) >> 1;
        int lc = i+1, rc = 2 * (m-l+1) + i;
 
        if (qr <= m)
            return query(lc, l, m, ql, qr);
 
        if (m < ql)
            return query(rc, m+1, r, ql, qr);
 
        return unite(query(lc, l, m, ql, qr), query(rc, m+1, r, ql, qr));
    }
 
    int unite(int a, int b) {
        return a + b;
    }
 
public:
    SegTree(int n) : n(n), tree(2*n) {}
 
    void update(int pos, int v) {
        update(0, 0, n-1, pos, v);
    }
 
    int query(int ql, int qr) {
        return query(0, 0, n-1, ql, qr);
    }
};
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, k;
    cin >> n >> k;
 
    int dp[n][k+1]{};
    vector<SegTree> segs(k+1, SegTree(n+1));
 
    int total = 0;
 
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
 
        segs[0].update(x, 1);
        dp[i][0] = 1;
 
        for (int j = 1; j <= k; j++) {
            dp[i][j] = segs[j-1].query(0, x-1);
            segs[j].update(x, dp[i][j]);
        }
 
        total += dp[i][k];
    }
 
    cout << total << endl;
}