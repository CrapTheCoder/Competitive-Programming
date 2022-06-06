bits/stdc++.h>
namespace std;

int long long
endl '\n'

pair<int, int>;

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

i, j;

pi farthest(int a, int b) {
int, pi> v1 = { abs(a-1) + abs(b-1), {1, 1} };
int, pi> v2 = { abs(a-1) + abs(b-m), {1, m} };
int, pi> v3 = { abs(a-n) + abs(b-1), {n, 1} };
int, pi> v4 = { abs(a-n) + abs(b-m), {n, m} };

max({v1, v2, v3, v4}).second;


main() {
sync_with_stdio(false);
tie(NULL);


t;
(t--) {
cin >> n >> m >> i >> j;

pair<int, int> fc = farthest(i, j);
pair<int, int> sc = {
(fc.first == 1) ? n : 1,
(fc.second == 1) ? m : 1


cout << fc.first << " " << fc.second << " " << sc.first << " " << sc.second << endl;

}