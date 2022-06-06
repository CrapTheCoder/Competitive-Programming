bits/stdc++.h>
namespace std;

main() {
cin >> n;
int, int> a;
int i = 0; i < n; i++) {
int x; cin >> x; a[x]++;


int, int> c;
auto [x, y]: a)
y]++;

cin >> q;
(q--) {
char t; int x;
cin >> t >> x;

a[x]]--;
(t == '-') a[x]--;
(t == '+') a[x]++;
a[x]]++;

bool square = false;
int pair_count = 0;

for (auto [i, j]: c) {
pair_count += i/2 * j;
if (i >= 4 && j > 0 && !square) {
pair_count -= 2;
square = true;
}


cout << ((square && pair_count >= 2) ? "YES" : "NO") << endl;

