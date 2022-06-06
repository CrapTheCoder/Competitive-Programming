#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int BLOCK = 450;
#define block(val) (val / BLOCK)
#define value(val) (cnt[val] * cnt[val] * val)
 
class Mo {
    struct query {
        int l, r, idx;
    };
 
    vector<int> a;
    vector<int> cnt;
    vector<query> qs;
 
public:
    Mo(const vector<int> &_a) : a(_a), cnt(*max_element(_a.begin(), _a.end()) + 1) {}
 
    void append(const int &l, const int &r) {
        qs.push_back({l, r, (int) qs.size()});
    }
 
    vector<int> solve() {
        sort(qs.begin(), qs.end(), [](query x, query y) {
            if (block(x.l) != block(y.l)) return x.l < y.l;
            return (block(x.l) & 1) ? (x.r > y.r) : (x.r < y.r);
        });
 
        vector<int> ans(qs.size());
 
        int cur = 0;
 
        auto add = [&](const int i) {
            cur -= value(a[i]);
            cnt[a[i]]++;
            cur += value(a[i]);
        };
 
        auto del = [&](const int i) {
            cur -= value(a[i]);
            cnt[a[i]]--;
            cur += value(a[i]);
        };
 
        for (int l = 0, r = -1, i = 0; i < qs.size(); i++) {
            while (l < qs[i].l) del(l++);
            while (r < qs[i].r) add(++r);
            while (l > qs[i].l) add(--l);
            while (r > qs[i].r) del(r--);
            
            ans[qs[i].idx] = cur;
        }
 
        return ans;
    }
};
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
    
    int n, t; cin >> n >> t;
 
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
 
    Mo mo(a);
    while (t--) {
        int l, r; cin >> l >> r;
        mo.append(l-1, r-1);
    }
 
    for (auto i : mo.solve())
        cout << i << endl;
}