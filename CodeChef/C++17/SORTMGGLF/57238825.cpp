#include <bits/stdc++.h>
using namespace std;

signed main() {
    int n; cin >> n;
    int a[n], b[n], c[n];

    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    
    for (int i = 0; i < n; i++)
        c[b[i]-1] = a[i];
    
    for (int i = 0; i < n; i++)
        cout << c[i] << " ";
}