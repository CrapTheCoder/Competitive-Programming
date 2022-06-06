bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

m;
n >> m;

= 0, end = 0;

ans = 0;
int c = 0; c < n; c++) {
string s; cin >> s;

int f = -1, l = -1;

for (int i = 0; i < m; i++) {
if (s[i] == 'W') {
l = i;
if (f == -1)
f = i;
}


(c != 0)
ans++;

(f == -1 || l == -1) {
end++;

else {
end = 0;

if (c % 2 == 0) ans += max(0LL, x - f), x = min(x, f);
if (c % 2 == 1) ans += max(0LL, l - x), x = max(x, l);

if (c % 2 == 0) ans += l - x, x = l;
if (c % 2 == 1) ans += x - f, x = f;
}
}

if (end == n)
end--;

cout << ans - end << endl;
}