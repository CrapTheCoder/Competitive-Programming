bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

string s; cin >> s;

f = false;
int i = 0; i + 26 <= s.size(); i++) {
map<char, int> a;
for (int j = i; j < i+26; j++)
a[s[j]]++;

bool flag = true;

vector<char> x;
for (char j = 'A'; j <= 'Z'; j++) {
if (a[j] == 0) x.push_back(j);
if (a[j] > 1) flag = false;


flag = flag && a['?'] == x.size();

(flag) {
for (int j = i; j < i+26; j++)
if (s[j] == '?')
s[j] = x.back(), x.pop_back();

for (int j = 0; j < s.size(); j++)
if (s[j] == '?')
s[j] = 'A';

cout << s << endl;
f = true;
break;
}
}

if (!f)
cout << -1 << endl;
}