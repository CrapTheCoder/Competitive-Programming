#include <bits/stdc++.h>
using namespace std;

#define speed ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)

#define endl '\n'
#define int long long

const int LEN = 25;
const int primes[LEN] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

int power(int x, int y, int m){
    int res = 1;

    while (y > 0){
        if (y & 1)
            res = (res * x) % m;

        y >>= 1;
        x = (x * x) % m;
    }

    return res;
}

signed main() {
    speed;

    int n; cin >> n;
    int a[n];

    for(int i = 0; i < n; i++)
        cin >> a[i];

    int pr[LEN][n+1];

    for(int i = 0; i < LEN; i++){
        pr[i][0] = 0;

        for(int j = 1; j <= n; j++){
            pr[i][j] = pr[i][j-1];

            while(a[j-1] % primes[i] == 0){
                pr[i][j]++;
                a[j-1] /= primes[i];
            }
        }
    }

    int t; cin >> t;

    while(t--){
        int l, r, m; cin >> l >> r >> m;

        int f = 1;

        for(int i = 0; i < LEN; i++){
            int cnt = pr[i][r] - pr[i][l-1];
            f = (f * power(primes[i], cnt, m)) % m;
        }

        cout << f << endl;
    }
}
