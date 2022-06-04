#include <iostream>
using namespace std;

#define endl '\n'
#define int long long

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int n; cin >> n;
        int m = n;
        bool x = false;

        while (m) {
            if (m % 2 == 0)
                x = true;

            m /= 10;
        }

        if (x)
            cout << 1;
        else
            cout << 0;

        cout << endl;
    }
}
