#include <bits/stdc++.h>
using namespace std;
 
#define int long long
 
signed main() {
    int n, m;
    cin >> n >> m;
 
    int cur = 0, t = 0;
    for (int i = 0; i < m; i++) {
        int x; cin >> x; x--;
        t += (x - cur + n) % n;
        cur = x;
    }
 
    cout << t << endl;
}