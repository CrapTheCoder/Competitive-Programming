#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;
    int a[n];
    int b[n+1];

    int cnt[2000];

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        cnt[a[i]]++;
    }

    for (int i = 0; i < n+1; i++) {
        cin >> b[i];
        cnt[b[i]]--;

        if (cnt[b[i]] < 0) {
            cout << b[i] << endl;
            break;
        }
    }
}
