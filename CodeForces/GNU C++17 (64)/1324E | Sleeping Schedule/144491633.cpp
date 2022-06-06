bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

l, r;
];
2013][2013];

int i = 0, int time = 0) {
== n)
return 0;

[i][time] != -1)
return dp[i][time];

s1 = (time + a[i]) % h;
s2 = (time + a[i] - 1) % h;

dp[i][time] = max(solve(i+1, s1) + (l <= s1 && s1 <= r), solve(i+1, s2) + (l <= s2 && s2 <= r));


main() {
sync_with_stdio(false); cin.tie(NULL);

n >> h >> l >> r;
int i = 0; i < n; i++)
cin >> a[i];

(dp, -1, sizeof dp);

<< solve() << endl;
