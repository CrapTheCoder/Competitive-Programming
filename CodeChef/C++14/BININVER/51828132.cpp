#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;

    while (tc--) {
        int n; cin >> n;

        int mini = INT_MAX;

        for (int i = 0; i < n; i++) {
            int x; cin >> x;

            int c = 0;
            while (x % 2 == 0) {
                x /= 2;
                c++;
            }

            mini = min(mini, c);
        }

        cout << mini << endl;
    }
}
