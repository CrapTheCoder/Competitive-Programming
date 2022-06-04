#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;
    while (n--) {
        int x; cin >> x;
        int nx = x;

        int s0 = 0;
        int s1 = 0;

        while (nx) {
            int d = nx % 10;

            if (d % 2 == 1) s1 += d;
            if (d % 2 == 0) s0 += d;

            nx /= 10;
        }

        if ((s1 % 3 == 0) || (s0 % 4 == 0))
            cout << "Yes ";
        else
            cout << "No ";
    }
}
