bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

<int> pals;
40013];

main() {
sync_with_stdio(false); cin.tie(NULL);

int i = 1; i <= 4e4 + 13; i++) {
string si = to_string(i);
string rev = si; ranges::reverse(rev);

(si == rev)
pals.push_back(i);


= 1;
int j : pals)
for (int i = 1; i <= 4e4; i++)
if (i - j >= 0)
dp[i] = (dp[i] + dp[i-j]) % MOD;

; cin >> tc;
(tc--) {
int n; cin >> n;
cout << dp[n] << endl;

