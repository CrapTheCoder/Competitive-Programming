#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
    int count = 0;
 
    while (n > 0) {
        while (n % 2 == 0)
            n /= 2;
 
        count++;
        n /= 2;
    }
 
    cout << count << endl;
}