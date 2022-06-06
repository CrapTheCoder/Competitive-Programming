bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

[113];

() {
cin >> n;
string s; cin >> s;

auto i: "14689") {
((int)s.find(i) != -1) {
cout << 1 << endl;
cout << i << endl;
return;



int i = 0; i < n; i++) {
for (int j = i+1; j < n; j++) {
if (!prime[stoi(string(1, s[i]) + string(1, s[j]))]) {
cout << 2 << endl;
cout << s[i] << s[j] << endl;
return;
}




main() {
sync_with_stdio(false); cin.tie(NULL);

prime, prime+113, true);
0] = prime[1] = false;
for (int i = 2; i < 113; i++)
if (prime[i])
for (int j = i*i; j < 113; j += i)
prime[j] = false;

int tc; cin >> tc;
while (tc--)
solve();
}