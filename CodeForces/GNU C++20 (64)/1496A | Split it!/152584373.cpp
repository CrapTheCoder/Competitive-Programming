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
int n, k; cin >> n >> k;
string s; cin >> s;

(k * 2 == n) {
cout << "NO" << endl;
continue;


string s1 = s.substr(0, k);
string s2 = s.substr(s.size() - k, k);
reverse(s2.begin(), s2.end());

(s1 == s2)
cout << "YES" << endl;
else
cout << "NO" << endl;

