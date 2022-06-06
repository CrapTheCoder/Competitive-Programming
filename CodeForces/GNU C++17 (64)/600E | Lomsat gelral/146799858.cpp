#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int INF = LLONG_MAX;
const int BLOCK = 600;
 
int n;
int oc[100013], st[100013], ed[100013], c[100013];
vector<int> tree[100013];
int tim = -1;
 
struct query {
    int l, r, u;
};
 
vector<query> qrs;
 
void dfs(int u=0, int p=-1) {
    st[u] = ++tim;
    c[tim] = oc[u];
 
    for (auto v : tree[u])
        if (v != p)
            dfs(v, u);
 
    ed[u] = tim;
    qrs.push_back({st[u], ed[u], u});
}
 
class Mo {
    vector<query> qs;
 
public:
    Mo(vector<query> qs) : qs(qs) {
        sort(qs.begin(), qs.end(), [&](query x, query y) {
            if (x.l / BLOCK != y.l / BLOCK) return x.l < y.l;
            return ((x.l / BLOCK) & 1) ? (x.r > y.r) : (x.r < y.r);
        });
    }
 
    void process() {
        int ans[qs.size()];
        int mp[n+5]{}, sum[n+5] = {INF};
 
        auto add = [&](int i) { sum[++mp[c[i]]] += c[i]; };
        auto del = [&](int i) { sum[mp[c[i]]--] -= c[i]; };
 
        int l = 0, r = -1;
 
        for (auto [cl, cr, u] : qs) {
            while (r < cr) add(++r);
            while (l > cl) add(--l);
            while (r > cr) del(r--);
            while (l < cl) del(l++);
 
            int fl = 0, fr = n;
            while (fl < fr) {
                int mid = (fl + fr + 1) >> 1;
                if (sum[mid] == 0)
                    fr = mid-1;
                else
                    fl = mid;
            }
 
            ans[u] = sum[fl];
        }
 
        for (int i = 0; i < qs.size(); i++)
            cout << ans[i] << " ";
 
        cout << endl;
    }
};
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> oc[i];
 
    for (int i = 0; i < n-1; i++) {
        int x, y; cin >> x >> y;
        x--; y--;
 
        tree[x].push_back(y);
        tree[y].push_back(x);
    }
 
    dfs();
 
    Mo mo(qrs);
    mo.process();
}