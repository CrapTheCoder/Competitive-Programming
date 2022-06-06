#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n, h;
        cin >> n >> h;
 
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        
        int l = 0, r = 1e18;
 
        while (l < r) {
            int k = l + (r - l) / 2;
            
            int d = 0;
            for (int i = 0; i < n-1; i++) {
                if (a[i+1] - a[i] < k)
                    d += a[i+1] - a[i];
                else
                    d += k;
            }
 
            d += k;
 
            // cout << k << " " << d << endl;
 
            if (d < h)
                l = k + 1;
            else
                r = k;
        }
 
        cout << l << endl;
    }
}