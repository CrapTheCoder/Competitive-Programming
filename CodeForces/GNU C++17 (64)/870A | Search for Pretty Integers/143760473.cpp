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
    int a[n], b[m];
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < m; i++) cin >> b[i];
 
    sort(a, a+n);
    sort(b, b+m);
 
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i] == b[j]) {
                cout << a[i]; return 0;
            }
        }
    }
 
    int x = *min_element(a, a+n);
    int y = *min_element(b, b+m);
 
    if (x > y)
        swap(x, y);
    
    cout << x << y << endl;
}