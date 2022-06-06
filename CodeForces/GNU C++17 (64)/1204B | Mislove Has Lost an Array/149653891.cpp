#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int mini(int n, int l) {
    int t = 0, c = 1;
    for (int i = 0; i < l; i++) {
        t += c; c *= 2;
    }
 
    return t + (n - l);
}
 
int maxi(int n, int r) {
    int t = 0, c = 1;
    for (int i = 0; i < r; i++) {
        t += c; c *= 2;
    }
 
    c /= 2;
    return t + (n - r) * c;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, l, r;
    cin >> n >> l >> r;
 
    cout << mini(n, l) << " " << maxi(n, r) << endl;
}