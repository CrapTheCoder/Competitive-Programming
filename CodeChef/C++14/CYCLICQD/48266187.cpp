#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long

signed main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;
    while (t--) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        if ((a + c == 180) && (b + d == 180))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}
