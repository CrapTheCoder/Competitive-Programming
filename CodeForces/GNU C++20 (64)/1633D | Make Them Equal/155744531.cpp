bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;


], c[1013], cost[4013];
1013][15013];

int i, int r) {
< 0) return -INF;
== n) return 0;

[i][r] != -1)
return dp[i][r];

dp[i][r] = max(solve(i+1, r - cost[b[i]]) + c[i], solve(i+1, r));


main() {
sync_with_stdio(false); cin.tie(NULL);

cost, cost+4013, INF); cost[1] = 0;
int i = 1; i < 2000; i++)
for (int x = 1; x <= i; x++)
cost[i + i/x] = min(cost[i] + 1, cost[i + i/x]);

; cin >> tc;
(tc--) {
cin >> n >> k;
memset(dp, -1, sizeof dp);

for (int i = 0; i < n; i++) cin >> b[i];
for (int i = 0; i < n; i++) cin >> c[i];

int s = accumulate(c, c+n, 0);

if (n*15 <= k) {
cout << s << endl;
continue;
}

cout << solve(0, k) << endl;
}
}