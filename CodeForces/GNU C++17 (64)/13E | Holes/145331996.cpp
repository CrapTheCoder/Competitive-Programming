#include <bits/stdc++.h>
 
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
const int BLOCK = 300;
 
class SqrtDecomp {
    struct value {
        int cnt, idx, last;
    };
 
    int n;
    vector<int> a;
    vector<value> sq;
 
    void build() {
        for (int i = 0; i < n; i++)
            if (sq[i].cnt == -1)
                build_block(i);
    }
 
    pair<int, int> query(int i) {
        int total = 0, last = -1;
 
        int cur = i;
        while (cur < n) {
            total += sq[cur].cnt;
            last = sq[cur].last;
            cur = sq[cur].idx;
        }
 
        return {total, last};
    }
 
    void build_block(int i) {
        int cur = i / BLOCK;
        int cur_beg = cur * BLOCK;
        int cur_end = min((cur + 1) * BLOCK - 1, n-1);
 
        for (int j = cur_end; j >= cur_beg; j--) {
            int nxt = j + a[j];
            if (nxt > cur_end)
                sq[j] = {1, nxt, j};
 
            else
                sq[j] = sq[nxt], sq[j].cnt++;
        }
    }
 
public:
    SqrtDecomp(vector<int> a) : n(a.size()), sq(a.size(), {-1, -1}), a(a) {
        build();
    }
 
    void update(int i, int v) {
        a[i] = v;
        build_block(i);
    }
 
    pair<int, int> get(int i) {
        return query(i);
    }
};
 
signed main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
 
    int n, m;
    cin >> n >> m;
 
    vector<int> p(n);
    for (int i = 0; i < n; i++)
        cin >> p[i];
 
    SqrtDecomp sd(p);
 
    while (m--) {
        int typ;
        cin >> typ;
 
        if (typ == 0) {
            int a, b;
            cin >> a >> b; a--;
            sd.update(a, b);
 
        } else {
            int a;
            cin >> a; a--;
            auto [total, idx] = sd.get(a);
            cout << idx+1 << " " << total << endl;
        }
    }
}