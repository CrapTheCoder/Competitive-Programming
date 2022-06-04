#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int INF = LLONG_MAX >> 1;

int fac[12];
int sol[10000013];

signed main() {
    fac[0] = 1;
    for (int i = 1; i <= 11; i++)
        fac[i] = fac[i-1] * i;

    sol[0] = 0;
    for (int i = 1; i < 10000013; i++) {
        sol[i] = INF;
        for (int j = 1; j <= 11; j++) {
            if (i - fac[j] >= 0)
                sol[i] = min(sol[i], sol[i - fac[j]] + 1);
        }
    }

    int n; cin >> n;
    cout << sol[n] << endl;
}
