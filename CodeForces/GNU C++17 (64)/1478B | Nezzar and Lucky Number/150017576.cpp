bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

(int n, int d) {
>= 10*d) {
cout << "YES" << endl;
return;


(n >= 0) {
-= d;
(n % 10 == 0) {
cout << "YES" << endl;
return;



<< "NO" << endl;


main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int n, d; cin >> n >> d;
while (n--) {
int x; cin >> x;
solve(x, d);


