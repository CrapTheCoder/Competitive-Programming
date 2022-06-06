#include <bits/stdc++.h>
using namespace std;
 
signed main() {
    int tc; cin >> tc;
    while (tc--) {
        int l, r, a;
        cin >> l >> r >> a;
 
        int val = (r / a) * a - 1;
 
        if (val < l) {
            cout << (r / a) + (r % a) << endl;
 
        } else {
            cout << max((val / a) + (val % a), (r / a) + (r % a)) << endl;
        }
    }
}