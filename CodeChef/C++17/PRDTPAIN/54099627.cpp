#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    int t; cin >> t;

    while (t--) {
        int n; cin >> n;

        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        
        int s = 0;
        for (int i = 0; i < n; i++) {
            int k = i+1;
            int maxi = 0;

            for (int j = i+2; j < n; j++) {
                int c = (a[j] - a[k]) * (a[k] - a[i]);
                bool flag = false;

                while (maxi <= c && k < j) {
                    maxi = c;
                    k++; c = (a[j] - a[k]) * (a[k] - a[i]);
                    flag = true;
                }

                if (flag)
                    k--;
                
                s += maxi;
            }
        }

        cout << s << endl;
    }
}
