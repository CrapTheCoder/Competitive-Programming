#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
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
 
        int ans = n-1;
        for (int i = n-1; i > 0; i--) {
            if (a[i] <= a[i-1])
                ans = i-1;
            else
                break;
        }
 
        for (int i = ans; i > 0; i--) {
            if (a[i] >= a[i-1])
                ans = i-1;
            else
                break;
        }
 
        cout << ans << endl;
    }
}