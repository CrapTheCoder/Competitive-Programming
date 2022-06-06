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
string x; int p;
cin >> x >> p;

string y; int q;
cin >> y >> q;

(x.size() + p == y.size() + q) {
while (x.size() < y.size()) x.push_back('0'), p--;
while (y.size() < x.size()) y.push_back('0'), q--;

if (stoi(x) < stoi(y))
cout << "<" << endl;
else if (stoi(x) == stoi(y))
cout << "=" << endl;
else
cout << ">" << endl;

else {
cout << ((x.size() + p < y.size() + q) ? "<" : ">") << endl;


