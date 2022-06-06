//Author: Shivank
#include<bits/stdc++.h>
 
using namespace std; using ll = long long int;
#define tc int t; cin >> t; while(t--)
 
void solve() {
    ll n; cin >> n;
 
    for (ll i = 1; i * i <= n; i++) {
        if (n == i * i * 2 || n == i * i * 4) {
            cout << "YES" << endl;
            return;
        }
    }
 
    cout << "NO" << endl;
}
 
int main() {
    ios_base::sync_with_stdio(0); cin.tie(nullptr);
 
    tc {
        solve();
    }
}