bits/stdc++.h>
namespace std;

int long long
endl '\n'
all(iter) (iter).begin(), (iter).end()
rall(iter) (iter).rbegin(), (iter).rend()

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

cin >> n;
string s; cin >> s;

string rm(10, '0');

auto c : s) {
(c == 'L') {
for (int i = 0; i <= 9; i++) {
if (rm[i] == '0') {
rm[i] = '1'; break;
}
}

else if (c == 'R') {
for (int i = 9; i >= 0; i--) {
if (rm[i] == '0') {
rm[i] = '1'; break;
}
}

else {
rm[c - '0'] = '0';



cout << rm << endl;
}