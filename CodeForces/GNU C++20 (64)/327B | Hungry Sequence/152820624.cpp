#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
const int MAX = 10000013;
bool sieve[MAX];
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n; cin >> n;
 
    fill(sieve, sieve+MAX, true);
 
    int cnt = 0;
    sieve[0] = sieve[1] = false;
    for (int i = 2; i < MAX; i++) {
        if (!sieve[i])
            continue;
 
        cnt++;
        cout << i << " ";
 
        if (cnt == n)
            break;
 
        for (int j = i*i; j < MAX; j += i)
            sieve[j] = false;
    }
 
    cout << endl;
}