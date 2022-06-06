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
string s; cin >> s;
char c; cin >> c;

bool flag = false;
for (int i = 0; i < s.size(); i++) {
if (s[i] == c && i % 2 == 0)
flag = true;


cout << (flag ? "YES" : "NO") << endl;

