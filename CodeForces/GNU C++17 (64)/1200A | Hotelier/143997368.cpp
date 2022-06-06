#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
    string s; cin >> s;
 
    string rm(10, '0');
 
    for (auto c : s) {
        if (c == 'L') {
            for (int i = 0; i <= 9; i++) {
                if (rm[i] == '0') {
                    rm[i] = '1'; break;
                }
            }
            
        } else if (c == 'R') {
            for (int i = 9; i >= 0; i--) {
                if (rm[i] == '0') {
                    rm[i] = '1'; break;
                }
            }
 
        } else {
            rm[c - '0'] = '0';
        }
    }
    
    cout << rm << endl;
}