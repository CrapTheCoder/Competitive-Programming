#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long

signed main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;
    while (t--) {
        int n, a, b;
        cin >> n >> a >> b;

        cout << (180 - a) + (180 - b) + 2 * n << endl;
    }
}
