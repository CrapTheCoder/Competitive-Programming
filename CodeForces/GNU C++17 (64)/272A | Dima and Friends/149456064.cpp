#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
 
    int s = 0;
    for (int i = 0; i < n; i++) {
        int x; cin >> x; s += x;
    }
 
    int c = 0;
    for (int i = s+1; i <= s+5; i++)
        if (i % (n+1) != 1)
            c++;
 
    cout << c << endl;
}