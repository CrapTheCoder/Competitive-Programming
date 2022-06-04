#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) iter.size();

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int n, q;
vector<pair<int, int>> g[500013];
int color[500013];
int cc[2];

bool solve(int u, int cur=0) {
    if (color[u] != -1)
        return color[u] == cur;

    color[u] = cur; cc[cur]++;
    for (auto vt : g[u]) {
        int v = vt.first, t = vt.second;
        if (!solve(v, t == 1 ? cur^1 : cur))
            return false;
    }
    
    return true;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        cin >> n >> q;

        for (int i = 0; i < n; i++) {
            g[i].clear();
            color[i] = -1;
        }

        for (int i = 0; i < q; i++) {
            int t, u, v;
            cin >> t >> u >> v;
            u--; v--;

            g[u].push_back({v, t});
            g[v].push_back({u, t});
        }

        int maxi = 0;
        bool flag = true;

        for (int u = 0; u < n; u++) {
            if (color[u] == -1) {
                cc[0] = cc[1] = 0;

                if (solve(u)) {
                    maxi += max(cc[0], cc[1]);

                } else {
                    flag = false;
                    break;
                }
            }
        }

        cout << (flag ? maxi : -1) << endl;
    }
}
