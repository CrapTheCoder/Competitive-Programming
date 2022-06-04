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
 
        int zero = 0;
        set<int> vals;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            if (x == 0)
                zero++;
 
            vals.insert(x);
        }
 
        if (zero)
            cout << n - zero << endl;
        
        else if (vals.size() != n)
            cout << n << endl;
            
        else
            cout << n + 1 << endl;
    }
}