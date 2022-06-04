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

    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    bool flag = false;
    for (int i = 0; i < min(a.size(), b.size()); i++)
        if ((a[i] - '0') + (b[i] - '0') > 9)
            flag = true;

    if (flag)
        cout << "Hard" << endl;
    else
        cout << "Easy" << endl;
}
