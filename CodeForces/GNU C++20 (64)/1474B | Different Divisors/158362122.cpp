#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
bool pc(int n) {
    for (int c = 2; c*c <= n; c++)
        if (n % c == 0)
            return false;
 
    return (n >= 2);
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int d; cin >> d;
 
        int p, q;
        for (p = d+1; ; p++)
            if (pc(p))
                break;
 
        for (q = d+p; ; q++)
            if (pc(q))
                break;
 
        cout << p*q << endl;
    }
}