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

map<char, int> mp;
for (int i = 0; i < s.size(); i++)
mp[s[i]]++;

for (int i = 0; i < s.size(); i++) {
if (mp[s[i]] == 1) {
cout << s.substr(i, s.size()) << endl;
break;
}

mp[s[i]]--;


