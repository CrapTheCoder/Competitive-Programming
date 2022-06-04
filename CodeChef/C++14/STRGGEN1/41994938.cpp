#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define INF INT_MAX

signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while (t--) {
        int n, m; cin >> n >> m;

        int a[n][26];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < 26; j++)
                a[i][j] = 0;

        for (int i = 0; i < n; i++) {
            string s; cin >> s;
            for (auto j : s)
                a[i][j-'a']++;
        }

        int i = 0;
        string s, t; cin >> s;

        for (auto j : s) {
            if (a[i][j-'a'] > 0) {
                a[i][j-'a']--;
                t += j;
            }

            else
                break;

            i = (i+1) % n;
        }

        if (s != t)
            cout << "No" << endl;
        else
            cout << "Yes" << endl;
    }
}
