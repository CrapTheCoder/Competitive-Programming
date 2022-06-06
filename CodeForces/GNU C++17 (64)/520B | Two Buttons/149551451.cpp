bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

m;
n >> m;

pair<int, int>> q;
({n, 0});

<int> vis;

(true) {
auto [cur, cur_dep] = q.front(); q.pop();

(vis.count(cur)) continue;
vis.insert(cur);

(cur == m) {
cout << cur_dep << endl;
break;


(cur-1 > 0)
q.push({cur-1, cur_dep + 1});

(cur*2 < 10013)
q.push({cur*2, cur_dep + 1});

