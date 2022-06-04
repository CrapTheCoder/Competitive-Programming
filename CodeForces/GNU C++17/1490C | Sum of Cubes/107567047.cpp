#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int t; cin >> t;
 
    while (t--) {
        int n; cin >> n;
 
        bool f = false;
 
        for (int i = 1; i <= 10000; i++) {
            int x = i*i*i;
 
            int d = pow((n - x), (double)1/3);
 
            for (int j = max(1LL, d-5); j < d+5; j++) {
                if (x + j*j*j == n) {
                    cout << "YES" << endl;
                    f = true;
                    break;
                }
            }
 
            if (f)
                break;
        }
 
        if (!f)
            cout << "NO" << endl;
    }
}