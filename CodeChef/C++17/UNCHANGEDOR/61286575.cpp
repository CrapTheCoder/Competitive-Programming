#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
        int count = 0;

        int on = n;
        while (n)
            n >>= 1, count++;

        cout << on - count << endl;
    }
}
