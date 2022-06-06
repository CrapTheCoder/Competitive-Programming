#include <bits/stdc++.h>
using namespace std;
 
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
 
using namespace __gnu_pbds;
#define oset tree<int, null_type, greater_equal<int>, rb_tree_tag, tree_order_statistics_node_update>
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
 
        int c = 0; oset s;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            c += s.order_of_key(x-1);
            s.insert(x);
        }
        
        cout << c << endl;
    }
}