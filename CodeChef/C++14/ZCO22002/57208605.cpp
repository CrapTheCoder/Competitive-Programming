#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;

        int a[m][n];
        map<int, int> c[m];

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                cin >> a[i][j], c[j][a[i][j]]++;
        
        vector<int> msg;

        for (int i = 0; i < m; i++) {
            bool flag = true;
            for (int j = 0; j < n; j++)
                flag = flag && (c[j][a[i][j]] == m/2);
            
            if (flag) msg.push_back(i);
        }

        if (msg.size() != 0) {
            set<int> vals;

            for (int i = 0; i < m; i++) {
                int cur = 0;
                for (int j = 0; j < n; j++)
                    if (a[i][j] != a[msg[0]][j])
                        cur |= (1 << j);
                
                vals.insert(cur);
            }

            if (vals.size() != m)
                msg.clear();
        }

        cout << msg.size() << endl;
        for (auto i : msg) cout << i << " ";
        cout << endl;
    }
}
