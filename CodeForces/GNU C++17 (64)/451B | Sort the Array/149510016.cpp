bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

cin >> n;
<int> a(n), b(n);
int i = 0; i < n; i++)
cin >> a[i], b[i] = a[i];

.begin(), b.end());

r;

l = 0; l < n; l++)
(a[l] != b[l])
break;

r = n-1; r >= 0; r--)
(a[r] != b[r])
break;

> r)
cout << "yes\n" << 1 << " " << 1 << endl;


reverse(a.begin() + l, a.begin() + r + 1);
(a == b)
cout << "yes\n" << l+1 << " " << r+1 << endl;
else
cout << "no" << endl;

}