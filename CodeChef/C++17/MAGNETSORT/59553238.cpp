#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];

        string parity; cin >> parity;

        vector<int> b = a;
        sort(b.begin(), b.end());

        // Already sorted
        if (a == b) {
            cout << 0 << endl;
            continue;
        }

        int first;  // First unsorted index
        bool north_till_first = false, south_till_first = false;  // To check if there's north/south from 0 to first

        int last;  // Last unsorted index
        bool north_till_last = false, south_till_last = false;  // To check if there's north/south from last to n-1

        for (int i = 0; i < n; i++) {
            if (parity[i] == 'N') north_till_first = true;
            if (parity[i] == 'S') south_till_first = true;

            if (a[i] != b[i]) {
                first = i; break;
            }
        }

        for (int i = n-1; i >= 0; i--) {
            if (parity[i] == 'N') north_till_last = true;
            if (parity[i] == 'S') south_till_last = true;

            if (a[i] != b[i]) {
                last = i; break;
            }
        }

        if ((north_till_first && south_till_last) || (north_till_last && south_till_first)) {
            cout << 1 << endl;
            continue;
        }

        if (find(parity.begin(), parity.end(), 'N') == parity.end() ||
            find(parity.begin(), parity.end(), 'S') == parity.end()) {
            cout << -1 << endl;
            continue;
        }

        cout << 2 << endl;
    }
}
