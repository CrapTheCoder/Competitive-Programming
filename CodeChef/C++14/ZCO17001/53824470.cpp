#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, t;
    cin >> n >> t;

    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    
    sort(a, a+n);

    int c = 0;

    unordered_map<int, int> mp;
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {
            if (a[i] + a[j] > t)
                break;

           if (mp.count(t - (a[i] + a[j])))
                c += mp[t - (a[i] + a[j])];
        }

        for (int j = 0; j < i; j++) {
            if (a[i] + a[j] > t)
                break;

            mp[a[i] + a[j]]++;
        }
    }
    
    cout << c << endl;
}
