bits/stdc++.h>
namespace std;

main() {
; cin >> tc;
(tc--) {
int n; cin >> n;

int a[n], maxi = 0;
for (int i = 0; i < n; i++)
cin >> a[i], maxi = max(maxi, a[i]);

bool flag = false;
for (int i = 0; i < n; i++) {
if ((i-1 >= 0) && (a[i-1] != maxi) && (a[i] == maxi)) {
flag = true;
cout << i+1 << endl;
break;
}

if ((i+1 < n) && (a[i+1] != maxi) && (a[i] == maxi)) {
flag = true;
cout << i+1 << endl;
break;
}


(!flag)
cout << -1 << endl;

