bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

cin >> n;
n];
int i = 0; i < n; i++)
cin >> a[i];

oc = count(a, a+n, 1);

oc == n) {
cout << oc - 1 << endl;
return 0;


maxi = oc;

int i = 0; i < n; i++) {
int c0 = 0, c1 = 0;
for (int j = i; j < n; j++) {
if (a[j] == 0) c0++;
if (a[j] == 1) c1++;

maxi = max(maxi, oc + c0 - c1);



<< maxi << endl;
