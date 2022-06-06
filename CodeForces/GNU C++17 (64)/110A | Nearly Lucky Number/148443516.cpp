bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

string s; cin >> s;

= 0;
auto i : s)
(i == '4' || i == '7')
c++;

string res = to_string(c);

flag = false;
auto i : res)
(i != '4' && i != '7')
flag = true;

flag)
cout << "NO" << endl;

cout << "YES" << endl;
