bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
string s, t; cin >> s >> t;
int n = s.size(), m = t.size();

bool poss = false;
for (int i = 0; i < n; i++) {
for (int j = i; j < n; j++) {
string res;
int k = j - (m - (j - i + 1));

for (int l = i; l < j; l++)
res += s[l];

for (int l = j; l >= k; l--) {
if (l < 0) goto skip;
res += s[l];
}

if (res == t)
poss = true;

skip:;
}


cout << (poss ? "YES" : "NO") << endl;
}
}