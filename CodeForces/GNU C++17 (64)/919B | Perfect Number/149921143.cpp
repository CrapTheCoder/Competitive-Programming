#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int sum(int n) {
    int c = 0;
 
    while (n)
        c += n % 10, n /= 10;
 
    return c;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int k; cin >> k;
 
    int count = 0;
 
    for (int i = 19; ; i += 9) {
        if (sum(i) == 10)
            count++;
 
        if (count == k) {
            cout << i << endl;
            break;
        }
    }
}