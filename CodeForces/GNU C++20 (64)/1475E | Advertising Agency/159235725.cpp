bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

int x, int y, int mod=0) {
mod)
%= MOD;

= 1;
(y) {
(y & 1)
z = mod ? (z*x) % mod : (z*x);

= mod ? (x*x) % mod : (x*x);
>>= 1;


z;


inverse(int d) {
power(d, MOD-2, MOD);


MAX = 1013;
];

int n, int r) {
f[n] * inverse(f[r] * f[n-r]) % MOD;


main() {
sync_with_stdio(false); cin.tie(NULL);

f[0] = 1;
for (int i = 1; i < MAX; i++)
f[i] = f[i-1] * i % MOD;

int tc; cin >> tc;
while (tc--) {
int n, k; cin >> n >> k;

int a[n];
for (int i = 0; i < n; i++)
cin >> a[i];

sort(a, a+n);

int cur, i;
for (i = n-1; i >= n-k; i--) {
if (i+1 == n || a[i] != a[i+1])
cur = 0;

cur++;
}

cout << ncr(count(a, a+n, a[i+1]), cur) << endl;
}
}