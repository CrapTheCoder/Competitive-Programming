bits/stdc++.h>
namespace std;

<ext/pb_ds/tree_policy.hpp>
<ext/pb_ds/assoc_container.hpp>

namespace __gnu_pbds;
oset tree<int, null_type, greater_equal<int>, rb_tree_tag, tree_order_statistics_node_update>

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int n; cin >> n;

int c = 0; oset s;
for (int i = 0; i < n; i++) {
int x; cin >> x;
c += s.order_of_key(x-1);
s.insert(x);


cout << c << endl;

