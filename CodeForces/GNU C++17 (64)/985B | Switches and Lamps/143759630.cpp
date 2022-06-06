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
 
    int n, m; cin >> n >> m;
 
    int b[m]{};
 
    char a[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
            if (a[i][j] == '1')
                b[j]++;
        }
    }
    
    bool flag2 = false;
    for (int i = 0; i < n; i++) {
        bool flag = false;
        for (int j = 0; j < m; j++) {
            if (a[i][j] == '1' && b[j] == 1) {
                flag = true; break;
            }
        }
 
        if (!flag) {
            flag2 = true;
            break;
        }
    }
 
    if (flag2) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}