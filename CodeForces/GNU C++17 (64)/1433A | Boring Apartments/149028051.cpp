bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

() {
cin >> x;

total = 0;
int i = 1; i <= 9; i++) {
int current_number = i;
int keypress = 0;

while (current_number < 10000) {
keypress++;
total += keypress;

if (current_number == x) {
cout << total << endl;
return;
}

current_number = current_number * 10 + i;




main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
solve();

