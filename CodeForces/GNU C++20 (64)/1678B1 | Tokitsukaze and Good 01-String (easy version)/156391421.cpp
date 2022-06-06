bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;



int> dp[200013][2];

int> solve(int i=0, int p=-1) {
== n)
return {0, 0};

!= -1 && dp[i][p].first != -1)
return dp[i][p];

i] == s[i+1]) {
auto ans = solve(i+2, s[i] - '0');
ans.second += (p != s[i] - '0');

(p != -1)
dp[i][p] = ans;

return ans;


ans1 = solve(i+2, 0);
first++; ans1.second += (p != 0);

ans2 = solve(i+2, 1);
first++; ans2.second += (p != 1);

!= -1)
[i][p] = min(ans1, ans2);

return min(ans1, ans2);
}

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

int tc; cin >> tc;
while (tc--) {
cin >> n >> s;

for (int i = 0; i <= n+3; i++)
dp[i][0] = dp[i][1] = {-1, -1};

auto ans = solve();
cout << ans.first << endl;
}
}