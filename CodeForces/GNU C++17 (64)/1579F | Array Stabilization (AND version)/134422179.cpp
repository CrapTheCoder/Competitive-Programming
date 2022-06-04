#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int n, d; cin >> n >> d;
        
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        
        int maxi = 0;
 
        queue<pair<int, int>> q;
        bool vis[n] = {false};
 
        for (int i = 0; i < n; i++) if (a[i] == 0) {
            q.emplace(i, 0); vis[i] = true;
        }
        
        while (!q.empty()) {
            auto [i, j] = q.front(); q.pop();
            
            int ni = (i + d) % n;
            if (!vis[ni]) {
                vis[ni] = true;
                q.emplace(ni, j+1);
                maxi = max(maxi, j+1);
            }
        }
        
        if (find(vis, vis+n, false) != (vis+n))
            cout << -1 << endl;
        else
            cout << maxi << endl;
    }
}