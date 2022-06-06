bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

solution() {
string s; cin >> s;
= s.size();

int i = n-2; i >= 0; i--) {
int t = (s[i] - '0') + (s[i + 1] - '0');
(t > 9) {
s[i] = t / 10 + '0';
s[i+1] = t % 10 + '0';
cout << s << endl;

return;



= (s[0] - '0') + (s[1] - '0');
t + '0';

<< s.substr(1, n-1) << endl;


main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--)
solution();
