#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    string a, b;
    cin >> a >> b;
    int n = a.size();

    int c1 = 0, c2 = 0;
    for (int i = 0; i < n-1; i++) {
        if (a[i] == b[i])
            continue;

        if (a[i] == b[i+1] && b[i] == a[i+1])
            c1++;

        if (a[i] != b[i])
            c2++;
    }

    if (a[n-1] != b[n-1])
        c2++;

    if ((c1 == 1 && c2 == 2) || (c1 == 0 && c2 == 0))
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}
