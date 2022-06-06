#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int a, b; cin >> a >> b;
 
    for (int cur = 1; ; cur++) {
        (cur % 2) ? (a -= cur) : (b -= cur);
        if (a < 0) { cout << "Vladik" << endl; break; }
        if (b < 0) { cout << "Valera" << endl; break; }
    }
}