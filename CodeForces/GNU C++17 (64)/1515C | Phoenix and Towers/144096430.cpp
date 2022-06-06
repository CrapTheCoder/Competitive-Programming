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
        int n, m, x;
        cin >> n >> m >> x;
 
        priority_queue<pair<int, int>> pq;
        for (int i = 0; i < m; i++)
            pq.push({0, i});
 
        int a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i]; a[i] *= -1;
        }
 
        int ind[n];
 
        for (int i = 0; i < n; i++) {
            auto r = pq.top(); pq.pop();
 
            ind[i] = r.second;
            pq.push({r.first + a[i], r.second});
        }
 
        int g[m]{};
        for (int i = 0; i < n; i++)
            g[ind[i]] += a[i];
        
        sort(g, g+m);
        if (abs(g[m-1] - g[0]) > x) {
            cout << "NO" << endl;
 
        } else {
            cout << "YES" << endl;
            for (int i = 0; i < n; i++)
                cout << ind[i]+1 << " ";
            cout << endl;
        }
    }
}