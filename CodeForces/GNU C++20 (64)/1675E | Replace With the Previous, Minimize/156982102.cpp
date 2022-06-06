bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
//    ios::sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int n, k; cin >> n >> k;
string s; cin >> s;

int i; char c = 'a';

for (i = 0; i < n; i++) {
if (s[i] - 'a' <= k)
c = max(c, s[i]);
else
break;


for (; c > 'a'; c--) {
k--;
for (int j = 0; j < n; j++)
if (s[j] == c)
s[j]--;


while (k-- && s[i] > 'a') {
c = s[i];
for (int j = 0; j < n; j++)
if (s[j] == c)
s[j]--;


cout << s << endl;
}
}