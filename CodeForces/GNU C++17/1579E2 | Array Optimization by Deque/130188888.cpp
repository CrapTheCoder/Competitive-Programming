#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
 
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
 
using namespace __gnu_pbds;
typedef tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
 
#define int long long
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int n; cin >> n;
 
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
 
        ordered_set b;
 
        int c = 0;
 
        for (int i = 0; i < n; i++) {
            int x = b.order_of_key(a[i]);
            int y = i - b.order_of_key(a[i] + 1);
 
            b.insert(a[i]);
 
            c += min(x, y);
        }
 
        cout << c << endl;
    }
}