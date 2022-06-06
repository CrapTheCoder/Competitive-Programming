bits/stdc++.h>
namespace std;

int long long
endl '\n'
all(iter) (iter).begin(), (iter).end()
rall(iter) (iter).rbegin(), (iter).rend()

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

m; cin >> n >> m;

m]{};

[n][m];
int i = 0; i < n; i++) {
for (int j = 0; j < m; j++) {
cin >> a[i][j];
if (a[i][j] == '1')
b[j]++;



flag2 = false;
int i = 0; i < n; i++) {
bool flag = false;
for (int j = 0; j < m; j++) {
if (a[i][j] == '1' && b[j] == 1) {
flag = true; break;
}


(!flag) {
flag2 = true;
break;
}
}

if (flag2) {
cout << "YES" << endl;
} else {
cout << "NO" << endl;
}
}