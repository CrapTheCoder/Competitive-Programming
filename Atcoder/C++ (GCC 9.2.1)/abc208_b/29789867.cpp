#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int INF = LLONG_MAX >> 1;

signed main() {
    int fac[12];
    fac[0] = 1;
    for (int i = 1; i <= 11; i++)
        fac[i] = fac[i-1] * i;

    int n; cin >> n;

    int sol[n+1]; sol[0] = 0;
    fill(sol+1, sol+n+1, INF);

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= 11; j++)
            if (i - fac[j] >= 0)
                sol[i] = min(sol[i], sol[i - fac[j]] + 1);

    cout << sol[n] << endl;
}
