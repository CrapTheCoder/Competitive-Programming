#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int n, m;
int a[213], b[213];
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];
 
    for (int k = 0; k <= (1 << 9); k++) {
        bool flag2 = false;
        for (int i = 0; i < n; i++) {
            bool flag = false;
            for (int j = 0; j < m; j++) {
                if (((a[i] & b[j]) | k) == k)
                    flag = true;
            }
            
            if (!flag) {
                flag2 = true;
                break;
            }
        }
        
        if (!flag2) {
            cout << k << endl;
            break;
        }
    }
}