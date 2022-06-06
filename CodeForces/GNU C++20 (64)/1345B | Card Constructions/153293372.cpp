#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    vector<int> s;
 
    int cards = 0;
    for (int i = 1; i <= 30000; i++) {
        cards += 2*i;
        s.push_back(cards);
        cards += i;
    }
 
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
 
        int c = 0;
 
        while (n >= 2) {
            c++;
            auto it = prev(upper_bound(s.begin(), s.end(), n));
            n -= *it;
        }
 
        cout << c << endl;
    }
}