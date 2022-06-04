#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int fac[12]; fac[0] = 1;
    for (int i = 1; i <= 11; i++)
        fac[i] = fac[i-1] * i;


    int n; cin >> n;
    int cnt = 0;

    for (int i = 11; i >= 1; i--) {
        while (n - fac[i] >= 0) {
            n -= fac[i];
            cnt++;
        }
    }

    cout << cnt << endl;
}
