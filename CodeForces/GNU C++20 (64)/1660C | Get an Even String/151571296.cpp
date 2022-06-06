bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;


200013][30][2];

int i, char p, int o) {
== s.size())
return (o == 1) ? INF : 0;

[i][p-'a'][o] != -1)
return dp[i][p-'a'][o];

== 1) {
(s[i] == p)
return dp[i][p-'a'][o] = min(solve(i+1, '{', o^1), solve(i+1, p, o) + 1);

return dp[i][p-'a'][o] = solve(i+1, p, o) + 1;

{
return dp[i][p-'a'][o] = min(solve(i+1, s[i], o^1), solve(i+1, '{', o) + 1);



main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
cin >> s;
for (int i = 0; i < s.size() + 5; i++)
for (int j = 0; j < 30; j++)
dp[i][j][0] = dp[i][j][1] = -1;

cout << solve(0, '{', 0) << endl;
}
}