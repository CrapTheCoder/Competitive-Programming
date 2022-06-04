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
        
        int odd = 0;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            
            if (x % 2)
                odd++;
        }
        
        cout << odd / 2 << endl;
    }
}
