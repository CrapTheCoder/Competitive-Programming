//Author: Shivank
#include<bits/stdc++.h>
 
using namespace std; using ll = long long int;
#define tc int t; cin >> t; while(t--)
 
void solve() {
    ll n; cin >> n;
    int a = sqrt(n/2), b = sqrt(n/4);
 
    if (a*a*2 == n || b*b*4 == n)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}
 
int main() {
    ios_base::sync_with_stdio(0); cin.tie(nullptr);
 
    tc {
        solve();
    }
}