#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) (iter).size();
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n, m, rb, cb, rd, cd;
        cin >> n >> m >> rb >> cb >> rd >> cd;
 
        int dr = 1, dc = 1;
        int t = 0;
 
        while (true) {
            if (rb == rd || cb == cd)
                break;
            
            if (0 >= rb + dr || rb + dr > n) dr *= -1;
            if (0 >= cb + dc || cb + dc > m) dc *= -1;
 
            rb += dr;
            cb += dc;
            t++;
        }
        
        cout << t << endl;
    }
}