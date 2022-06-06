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
        int n, s; cin >> n >> s;
 
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        
        int l = 0, r = 0;
        int sum = s;
 
        int maxi = -1;
        int maxl = -1, maxr = -1;
 
        while (r < n) {
            sum += a[r];
 
            if (sum >= 0) {
                if (r-l+1 > maxi) {
                    maxi = r-l+1;
                    maxl = l; maxr = r;
                }
 
                r++;
 
            } else {
                sum -= a[l++];
                if (l <= r)
                    sum -= a[r];
            }
 
            if (l > r)
                r = l;
        }
 
        if (maxi == -1)
            cout << -1 << endl;
 
        else {
            cout << maxl+1 << " " << maxr+1 << endl;
        }
    }
}