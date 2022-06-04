#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;

    while (tc--) {
        int x, y; cin >> x >> y;

        if (abs(x) % 2 == abs(y) % 2)
            cout << "YES";
        else
            cout << "NO";

        cout << endl;
    }
}
