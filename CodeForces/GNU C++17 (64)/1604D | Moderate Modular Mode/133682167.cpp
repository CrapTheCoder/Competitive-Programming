#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
signed main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int x, y; cin >> x >> y;
 
        if (x == y) {
            cout << x << endl;
            continue;
        }
 
        if (x > y) {
            cout << x + y << endl;
            continue;
        }
 
        cout << y - ((y - x) / 2) % (x / 2) << endl;
    }
}