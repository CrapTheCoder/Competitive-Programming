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
int n; cin >> n;

int p[n];
for (int i = 0; i < n; i++)
cin >> p[i];

for (int i = 0; i < n; i++) {
int j = i;

for (int k = i+1; k < n; k++) {
if (p[i] < p[j] && p[j] > p[k]) {
cout << "YES" << endl;
cout << i+1 << " " << j+1 << " " << k+1 << endl;
goto end_loop;
}

if (p[k] > p[j])
j = k;
}


cout << "NO" << endl;
end_loop: ;

