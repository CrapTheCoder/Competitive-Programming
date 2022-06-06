bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

int n, int l) {
= 0, c = 1;
int i = 0; i < l; i++) {
+= c; c *= 2;


t + (n - l);


int n, int r) {
= 0, c = 1;
int i = 0; i < r; i++) {
+= c; c *= 2;


;
t + (n - r) * c;


main() {
sync_with_stdio(false); cin.tie(NULL);

l, r;
n >> l >> r;

<< mini(n, l) << " " << maxi(n, r) << endl;
