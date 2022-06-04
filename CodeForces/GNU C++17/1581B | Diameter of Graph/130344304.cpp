#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int n, m, k; cin >> n >> m >> k;
 
        if (m > (n * (n-1) / 2)) {
            cout << "NO" << endl;
            continue;
        }
 
        if (m+1 < n) {
            cout << "NO" << endl;
            continue;
        }
 
        if (n == 1) {
            if (k >= 2)
                cout << "YES" << endl;
            else
                cout << "NO" << endl;
 
            continue;
        }
 
        if (k <= 2) {
            cout << "NO" << endl;
            continue;
        }
 
        if (k == 3) {
            if (m == (n * (n-1) / 2))
                cout << "YES" << endl;
            else
                cout << "NO" << endl;
 
            continue;
        }
 
        if (k > 3)
            cout << "YES" << endl;
    }
}