#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, m;
    cin >> n >> m;
 
    if (m % n != 0) {
        cout << -1 << endl;
        return 0;
    }
 
    n = m / n;
 
    int c2 = 0, c3 = 0;
 
    while (n % 2 == 0) {
        n /= 2;
        c2++;
    }
 
    while (n % 3 == 0) {
        n /= 3;
        c3++;
    }
 
    if (n != 1) {
        cout << -1 << endl;
        return 0;
    }
 
    cout << c2 + c3 << endl;
}