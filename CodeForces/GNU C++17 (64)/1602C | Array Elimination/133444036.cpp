#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
using namespace std;
 
const int INF = LLONG_MAX >> 1;
 
signed main(){
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
 
    while (tc--) {
        int n; cin >> n;
 
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
 
        int cnt[40] = {0};
 
        for (int i = 0; i < n; i++)
            for (int j = 0; a[i] >> j; j++)
                if ((a[i] >> j) & 1)
                    cnt[j]++;
 
        for (int i = 1; i <= n; i++) {
            bool flag = false;
            for (int j = 0; j < 40; j++) {
                if (cnt[j] % i != 0) {
                    flag = true;
                    break;
                }
            }
 
            if (!flag)
                cout << i << " ";
        }
 
        cout << endl;
    }
}