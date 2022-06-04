#include <bits/stdc++.h>

using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int a, b; cin >> a >> b;
    int n = __gcd(a, b);

    int c = 0;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            c++;
            while (n % i == 0)
                n /= i;
        }
    }

    if (n > 1)
        c++;

    cout << c + 1 << endl;
}
