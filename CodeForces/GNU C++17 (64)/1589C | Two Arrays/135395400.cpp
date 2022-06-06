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
        int n; cin >> n;
 
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        
        int b[n];
        for (int i = 0; i < n; i++)
            cin >> b[i];
        
        sort(a, a+n);
        sort(b, b+n);
 
        bool flag = false;
        for (int i = 0; i < n; i++) {
            int diff = b[i] - a[i];
            if (!(0 <= diff && diff <= 1)) {
                flag = true; break;
            }
        }
 
        if (flag)
            cout << "NO" << endl;
        else
            cout << "YES" << endl;
    }
}