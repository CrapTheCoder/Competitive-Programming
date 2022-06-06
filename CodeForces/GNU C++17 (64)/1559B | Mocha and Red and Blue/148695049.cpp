bits/stdc++.h>
namespace std;

int long long
endl '\n'




string> dp[113][3];

string> solve(int i, int j=0) {
== n)
return {0, ""};

[i][j].first != -1)
return dp[i][j];

i] == '?') {
pair<int, string> v1 = solve(i+1, 1);
.first += (j == 1);
.second += "R";

pair<int, string> v2 = solve(i+1, 2);
.first += (j == 2);
.second += "B";

return dp[i][j] = min(v1, v2);


i] == 'R') {
pair<int, string> v1 = solve(i+1, 1);
.first += (j == 1);
.second += "R";
return dp[i][j] = v1;


i] == 'B') {
pair<int, string> v2 = solve(i+1, 2);
v2.first += (j == 2);
v2.second += "B";
return dp[i][j] = v2;
}
}

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

int tc; cin >> tc;
while (tc--) {
cin >> n;
cin >> s;

for (int i = 0; i <= n+5; i++)
dp[i][0] = dp[i][1] = dp[i][2] = {-1, ""};

string ans = solve(0).second;
reverse(ans.begin(), ans.end());

cout << ans << endl;
}
}