#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
int n, m, k;
 
bool f(int x) {
    int c = 0;
    for (int i = 1; i <= n; i++) {
        int l=0, r=m+1;
        while (l+1 < r) {
            int mid = l + (r - l) / 2;
            if (mid*i < x)
                l = mid;
            else
                r = mid;
        }
 
        c += l;
    }
 
    return c < k;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    cin >> n >> m >> k;
 
    int l = 0, r = n*m+1;
    while (l+1 < r) {
        int mid = l + (r - l) / 2;
        
        if (f(mid))
            l = mid;
        else
            r = mid;
    }
 
    cout << l << endl;
}