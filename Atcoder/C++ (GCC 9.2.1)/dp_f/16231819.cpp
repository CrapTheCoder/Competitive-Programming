#include <bits/stdc++.h>
using namespace std;

signed main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    string s, t;
    cin >> s >> t;

    int n = s.size();
    int m = t.size();

    int table[n+1][m+1];

    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++)
            table[i][j] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            table[i][j] = max(table[i-1][j], table[i][j-1]);

            if (s[i-1] == t[j-1])
                table[i][j] = max(table[i][j], table[i-1][j-1] + 1);
        }
    }

    // for (int i = 0; i <= n; i++) {
    //     for (int j = 0; j <= m; j++)
    //         cout << table[i][j] << " ";
    //
    //     cout << endl;
    // }

    string r;

    for (int i = n, j = m; i > 0 && j > 0;) {
        if (s[i-1] == t[j-1]) {
            r += s[i-1];
            --i, --j;
        } else if (table[i-1][j] == table[i][j]) {
            --i;
        } else if (table[i][j-1] == table[i][j]) {
            --j;
        }
    }

    reverse(r.begin(), r.end());

    cout << r << '\n';
}
