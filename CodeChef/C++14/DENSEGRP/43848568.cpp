#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

int n, m, x, y;
int edg[200013][4];
vector<int> lw, up;

bool check(int a, int b) {
    for (int i = 0; i < min(lw.size(), up.size()); i++)
        if ((lw[i] <= b) && (up[i] >= a))
            return true;

    return false;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;
    while (t--) {
        cin >> n >> m >> x >> y;
        x--; y--;

        for (int i = 0; i < m; i++) {
            cin >> edg[i][0] >> edg[i][1] >> edg[i][2] >> edg[i][3];
            edg[i][0]--; edg[i][1]--; edg[i][2]--; edg[i][3]--;
        }

        if (x == y) {
            cout << 0 << endl;
            continue;
        }

        int mini = INT_MAX;
        bool vis[m] = {false};
        lw.push_back(x); up.push_back(x);

        int cur = 0;

        while (lw.size() && up.size()) {
            cur += 1;

            vector<int> lw1, up1;
            for (int u = 0; u < m; u++) {
                if ((!vis[u]) && check(edg[u][0], edg[u][1])) {
                    vis[u] = true;

                    if ((edg[u][2] <= y) && (y <= edg[u][3]))
                        mini = min(mini, cur);

                    lw1.push_back(edg[u][2]);
                    up1.push_back(edg[u][3]);
                }
            }

            lw = lw1; up = up1;
        }

        lw.clear();
        up.clear();

        if (mini == INT_MAX)
            cout << -1 << endl;
        else
            cout << mini << endl;
    }
}
