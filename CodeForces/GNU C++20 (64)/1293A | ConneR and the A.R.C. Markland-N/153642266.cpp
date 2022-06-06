bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int n, s, k;
cin >> n >> s >> k;

vector<int> v1 = {0}, v2 = {n+1};
for (int i = 0; i < k; i++) {
int x; cin >> x;
if (x <= s) v1.push_back(x);
if (x >= s) v2.push_back(x);


sort(v1.rbegin(), v1.rend());
sort(v2.begin(), v2.end());

int l = s, r = s;
int d1 = INF, d2 = INF;

for (int i = 0; i < v1.size(); i++, l--) {
if (v1[i] != l) {
d1 = s - l;
break;
}


for (int i = 0; i < v2.size(); i++, r++) {
if (v2[i] != r) {
d2 = r - s;
break;
}
}

cout << min(d1, d2) << endl;
}
}