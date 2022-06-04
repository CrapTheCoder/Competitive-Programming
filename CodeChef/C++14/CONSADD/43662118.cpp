#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int n, m, x;
        cin >> n >> m >> x;

        int a[n][m];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> a[i][j];

        int s = 0;
        for (int i = 0; i < n; i++) {
            int f;
            for (int j = 0; j < m; j++) {
                cin >> f;
                a[i][j] -= f;
                s += a[i][j];
            }
        }

        if (s % x) {
            cout << "No" << endl;
            continue;
        }

        bool flag = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int v = a[i][j];

                if (j+x <= m)
                    for (int k = j; k < j+x; k++)
                        a[i][k] -= v;

                else if (i+x <= n)
                    for (int k = i; k < i+x; k++)
                        a[k][j] -= v;

                if (a[i][j])
                    flag = true;
            }
        }

        if (flag)
            cout << "No" << endl;
        else
            cout << "Yes" << endl;
    }
}
