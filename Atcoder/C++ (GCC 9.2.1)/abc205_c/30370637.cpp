#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int a, b, c; cin >> a >> b >> c;

    int power_a, power_b;

    if (c % 2 == 1) power_a = a, power_b = b;
    if (c % 2 == 0) power_a = a*a, power_b = b*b;

    if (power_a < power_b) cout << "<" << endl;
    if (power_a > power_b) cout << ">" << endl;
    if (power_a == power_b) cout << "=" << endl;
}
