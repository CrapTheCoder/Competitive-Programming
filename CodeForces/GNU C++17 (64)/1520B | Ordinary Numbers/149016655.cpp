#include <bits/stdc++.h>
using namespace std;
 
#define int long long
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int n; cin >> n;
 
        int count = 0;
        for (int d = 1; d <= 9; d++) {
            int cur = d;
            if (cur <= n)
                count++;
 
            for (int i = 0; i < 10; i++) {
                cur = cur * 10 + d;
                if (cur <= n)
                    count++;
            }
        }
 
        cout << count << endl;
    }
}