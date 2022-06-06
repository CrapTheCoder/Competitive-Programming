bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
string s; cin >> s;
int n = s.size();

int suf0[n+1]{}, suf1[n+1]{};
for (int i = n-1; i >= 0; i--) {
suf0[i] = suf0[i+1]; if (s[i] == '0') suf0[i]++;
suf1[i] = suf1[i+1]; if (s[i] == '1') suf1[i]++;


int ans = max(ranges::count(s, '0'), n - ranges::count(s, '1'));

int c0 = 0, c1 = 0;
for (int i = 0; i <= n; i++) {
int l = i-1, r = n;
while (r-l > 1) {
int m = (l + r) / 2;
if (c1 + suf1[m] < suf0[i] - suf0[m+1])
r = m;
else
l = m;
}

ans = min(ans, max(suf0[i] - suf0[l+1], c1 + suf1[l+1]));

if (s[i] == '0') c0++;
if (s[i] == '1') c1++;
}

cout << ans << endl;
}
}