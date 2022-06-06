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
+= "~";

int cur_count = 1;

set<char> ans;
for (int i = 1; i < s.size(); i++) {
if (s[i] == s[i-1])
cur_count++;

else {
if (cur_count % 2 == 1)
ans.insert(s[i-1]);

cur_count = 1;
}


for (auto i : ans)
cout << i;
cout << endl;

