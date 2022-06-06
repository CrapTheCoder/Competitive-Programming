#include<bits/stdc++.h>
using namespace std;
#define int long long
 
signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, sx, sy;
    cin >> n >> sx >> sy;
 
    int c1 = 0;
    int c2 = 0;
    int c3 = 0;
    int c4 = 0;
 
    for(int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
 
        if (x < sx) c1++;
        if (x > sx) c2++;
        if (y < sy) c3++;
        if (y > sy) c4++;
    }
 
    int m = max(max(c1, c2), max(c3, c4));
 
    cout << m << '\n';
 
    if (c1 == m) cout << sx - 1 << " " << sy << '\n';
    else if (c2 == m) cout << sx + 1 << " " << sy << '\n';
    else if (c3 == m) cout << sx << " " << sy - 1 << '\n';
    else if (c4 == m) cout << sx << " " << sy + 1 << '\n';
}