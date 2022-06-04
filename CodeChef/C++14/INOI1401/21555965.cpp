#include <cstring>
#include <bits/stdc++.h>

#define ll long long

using namespace std;

ll n, m, d;

int gr[310][310];
ll dp[310][310][310][2];

ll countWays(ll c1, ll c2, ll cou, int last){
    if(c1 == n-1 && c2 == m-1)
        return 1;
    if(c1 >= n || c2 >= m || gr[c1][c2] == 0)
        return 0;
    if(dp[c1][c2][cou][last] != -1)
        return dp[c1][c2][cou][last];

    ll x = 0;

    if(last == 1){
        if(cou < d)
            x = (x + countWays(c1 + 1, c2, cou + 1, 1)) % 20011;
        x = (x + countWays(c1, c2 + 1, 1, 0)) % 20011;
    }

    else {
        x = (x + countWays(c1 + 1, c2, 1, 1)) % 20011;
        if(cou < d)
            x = (x + countWays(c1, c2 + 1, cou + 1, 0)) % 20011;
    }

    return dp[c1][c2][cou][last] = x;
}

int main()
{
    cin >> n >> m >> d;

    for(ll i = 0; i < n; i++){
        for(ll j = 0; j < m; j++){
            cin >> gr[i][j];
        }
    }

    memset(dp, -1, sizeof(dp));

    cout << countWays(0, 0, 0, 0);

    return 0;
}
