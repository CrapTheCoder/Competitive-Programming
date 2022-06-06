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
 
    int c = 0;
    while (m > n) {
        if (m % 2)
            c++, m++;
        m /= 2; c++;
    }
 
    cout << c + (n - m) << endl;
}