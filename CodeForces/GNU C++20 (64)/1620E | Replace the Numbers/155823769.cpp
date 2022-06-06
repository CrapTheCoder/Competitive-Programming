bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

<pair<int, int>> v;

cin >> q;
(q--) {
int t; cin >> t;
(t == 1) {
int x; cin >> x;
v.push_back({x, -1});

else {
int x, y; cin >> x >> y;
v.push_back({x, y});



reverse(v.begin(), v.end());

<int> a;

int, int> c;
int i = 0; i <= 5e5 + 13; i++)
i] = i;

auto [x, y] : v) {
(y == -1)
a.push_back(c[x]);
else
c[x] = c[y];
}

reverse(a.begin(), a.end());

for (auto i : a)
cout << i << " ";
cout << endl;
}