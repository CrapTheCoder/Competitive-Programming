#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;

    while (tc--) {
        int n, m, k; cin >> n >> m >> k;
        int c[n]; for (int i = 0; i < n; i++) cin >> c[i];
        int t[n]; for (int i = 0; i < n; i++) cin >> t[i];

        map<int, vector<int>> l;

        for (int i = 0; i < n; i++)
            l[c[i]-1].push_back(t[i]);

        vector<int> f;

        for (int i = 0; i < m; i++) {
            if (l[i].size() == 0)
                continue;

            sort(l[i].begin(), l[i].end());

            f.push_back(l[i][0]);
            for (int j = 2; j < l[i].size(); j += 2)
                f.push_back(l[i][j] + l[i][j-1]);
        }

        sort(f.begin(), f.end());
        int g = 0;

        for (auto i : f) {
            if (k - i < 0)
                break;

            g++;
            k -= i;
        }

        cout << g << endl;
    }
}
