#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
 
    int oc = count(a, a+n, 1);
 
    if (oc == n) {
        cout << oc - 1 << endl;
        return 0;
    }
 
    int maxi = oc;
 
    for (int i = 0; i < n; i++) {
        int c0 = 0, c1 = 0;
        for (int j = i; j < n; j++) {
            if (a[j] == 0) c0++;
            if (a[j] == 1) c1++;
 
            maxi = max(maxi, oc + c0 - c1);
        }
    }
 
    cout << maxi << endl;
}