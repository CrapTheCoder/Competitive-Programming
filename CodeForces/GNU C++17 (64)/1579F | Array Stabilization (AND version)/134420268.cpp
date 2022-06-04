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
        
        bool flag = true;
        int maxi = 0;
 
        bool vis[n] = {false};
        for (int i = 0; i < n; i++) if (!vis[i]) {
            vector<int> cur;            
            int j = i;
            
            bool flag2 = false;
            do {
                if (a[j] == 0)
                    flag2 = true;
 
                cur.push_back(a[j]);
 
                vis[j] = true;
                j = (j + d) % n;
 
            } while (j != i);
 
            if (!flag2) {
                flag = false;
                break;
            }
 
            int r = cur.size();
            for (int i = 0; i < r; i++)
                cur.push_back(cur[i]);
            
            int m = cur.size();
            int last = -1;
 
            for (int i = 0; i < m; i++) {
                if (cur[i] == 0) {
                    last = i;
                } else if (last >= 0) {
                    maxi = max(maxi, i - last);
                }
            }
        }
 
        if (flag)
            cout << maxi << endl;
        else
            cout << -1 << endl;
    }
}