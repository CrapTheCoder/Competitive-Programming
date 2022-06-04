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
        int s = 0;

        while (m) {
            s += m % 10;
            m /= 10;
        }

        if (n % s == 0)
            cout << "Yes";
        else
            cout << "No";

        cout << endl;
    }
}
