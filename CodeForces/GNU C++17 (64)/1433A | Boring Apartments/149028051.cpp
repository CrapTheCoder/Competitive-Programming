#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
void solve() {
    int x; cin >> x;
 
    int total = 0;
    for (int i = 1; i <= 9; i++) {
        int current_number = i;
        int keypress = 0;
 
        while (current_number < 10000) {
            keypress++;
            total += keypress;
 
            if (current_number == x) {
                cout << total << endl;
                return;
            }
 
            current_number = current_number * 10 + i;
        }
    }
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        solve();
    }
}