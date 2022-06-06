#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int MAX = 1e6 + 13;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    bool sieve[MAX];
    fill(sieve, sieve + MAX, true);
    sieve[0] = sieve[1] = false;
 
    unordered_set<int> s;
 
    for (int i = 2; i < MAX; i++) {
        if (sieve[i]) {
            s.insert(i*i);
            for (int j = i * i; j < MAX; j += i)
                sieve[j] = false;
        }
    }
 
    int n; cin >> n;
    while (n--) {
        int x; cin >> x;
        if (s.count(x))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}