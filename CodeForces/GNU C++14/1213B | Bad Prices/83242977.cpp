#include <bits/stdc++.h>
using namespace std;
 
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
 
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
 
#define endl '\n'
 
signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int t; cin >> t;
 
    while(t--){
        int n; cin >> n;
 
        int a[n];
 
        for(int i = 0; i < n; i++)
            cin >> a[i];
 
        ordered_set x;
 
        int c = 0;
 
        for(int i = n-1; i >= 0; i--){
            x.insert(a[i]);
 
            if(x.order_of_key(a[i]) != 0)
                c++;
        }
 
        cout << c << endl;
    }
}