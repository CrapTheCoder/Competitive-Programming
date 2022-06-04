#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) (iter).size();

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
        map<int, int> cnt;

        for (int i = 2; i*i <= n; i++)
            while (n % i == 0)
                n /= i, cnt[i]++;
        
        if (n != 1)
            cnt[n]++;

        int mx = 0, mv = 0;
        for (auto [x, y] : cnt) 
            if (y > mx)
                mx = y, mv = x;

        cout << mv << endl;
    }
}
