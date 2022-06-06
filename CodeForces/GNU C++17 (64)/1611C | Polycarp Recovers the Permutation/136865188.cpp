#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
        
        int a[n], b[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            b[i] = a[i];
        }
        
        reverse(b, b+n);
        
        int i = 0, j = n-1;
        deque<int> d;
 
        while (i < j) {
            if (b[i] < b[j])
                d.push_front(b[i++]);
            else
                d.push_back(b[j--]);
        }
        
        bool flag1 = true, flag2 = true;
 
        d.push_back(b[i]);
        for (int i = 0; i < n; i++) {
            if (d[i] != a[i]) {
                flag1 = false;
                break;
            }
        }
        
        d.pop_back();
        d.push_front(b[i]);
 
        for (int i = 0; i < n; i++) {
            if (d[i] != a[i]) {
                flag2 = false;
                break;
            }
        }
 
        if (flag1 || flag2) {
            for (int i = 0; i < n; i++)
                cout << b[i] << " ";
            cout << endl;
 
        } else {
            cout << -1 << endl;
        }
    }
}