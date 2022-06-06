#include <bits/stdc++.h>
using namespace std;
 
signed main() {
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
 
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
 
        sort(a, a+n);
 
        int c0 = 0, c1 = 0;
        for (auto i : a) {
            if (c0 == i) c0++;
            else if (c1 == i) c1++;
        }
 
        cout << c0 + c1 << endl;
    }
}