#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define int long long
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
bool prime[113];
 
void solve() {
    int n; cin >> n;
    string s; cin >> s;
 
    for (auto i: "14689") {
        if ((int)s.find(i) != -1) {
            cout << 1 << endl;
            cout << i << endl;
            return;
        }
    }
 
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            if (!prime[stoi(string(1, s[i]) + string(1, s[j]))]) {
                cout << 2 << endl;
                cout << s[i] << s[j] << endl;
                return;
            }
        }
    }
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    fill(prime, prime+113, true);
    prime[0] = prime[1] = false;
    for (int i = 2; i < 113; i++)
        if (prime[i])
            for (int j = i*i; j < 113; j += i)
                prime[j] = false;
 
    int tc; cin >> tc;
    while (tc--)
        solve();
}