#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
class SegTree {
    int n;
    vector<int> tree;
 
    void update(int i, int l, int r, int k, int v) {
        if (l == r) {
            tree[i] += v;
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
 
    int unite(int a, int b) {
        return a + b;
    }
 
    public:
    SegTree(int _n) : n(_n), tree(2 * _n) {
 
    }
 
    void update(int k, int v) {
        update(0, 0, n-1, k, v);
    }
 
    int query(int a, int b) {
        if (a > b)
            return 0;
 
        return query(0, 0, n-1, a, b);
    }
};
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
    
    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    
    int b[n]; map<int, int> mp;
    for (int i = 0; i < n; i++)
        b[i] = ++mp[a[i]];
    
    int ans = 0;
 
    SegTree seg(n); mp.clear();
    for (int i = n-1; i >= 0; i--) {
        ans += seg.query(1, b[i]-1);
        seg.update(++mp[a[i]], 1);
    }
 
    cout << ans << endl;
}