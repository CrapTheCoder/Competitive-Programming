#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m, w, b;
    cin >> n >> m >> w >> b;

    map<int, vector<pair<int, int>>> d;

    int t = 0;

    for (int i = 0; i < w; i++) {
        int x, y; cin >> x >> y;
        d[x].push_back({y, 0});
    }

    for (int i = 0; i < b; i++) {
        int x, y; cin >> x >> y;
        d[x].push_back({y, 1});
    }

    for (int k = 1; k <= n; k++) {
        vector<pair<int, int>> a = d[k];
        a.push_back({0, -1});
        sort(a.begin(), a.end());

        int r = a.size();

        int f = 0;

        for (int i = 1; i < r; i++) {
            if (a[i].second == 1)
                f += (a[i].first - a[i-1].first) * (a[i].first - a[i-1].first + 1) / 2 - 1;

            if (a[i].second == 0) {
                if (i + 1 < r) {
                    int p1 = (a[i+1].first - a[i-1].first) * (a[i+1].first - a[i-1].first + 1) / 2 - 1;
                    int p2 = (a[i+1].first - a[i].first + 1) * (a[i+1].first - a[i].first + 2) / 2 - 1;

                    f += p1 - p2;

                } else {
                    int p1 = (m - a[i-1].first) * (m - a[i-1].first + 1) / 2 - 1;
                    int p2 = (m - a[i].first + 1) * (m - a[i].first + 2) / 2 - 1;

                    f += p1 - p2;
                }
            }
        }

        f += (m - a[r-1].first) * (m - a[r-1].first + 1) / 2;

        t += f;
    }

    cout << t << endl;
}
