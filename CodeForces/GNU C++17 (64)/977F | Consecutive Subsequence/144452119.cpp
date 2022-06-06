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

int, int> dp;
int i = 0; i < n; i++)
[a[i]] = max(dp[a[i]], dp[a[i]-1] + 1);

maxi = 0, maxv = -1;
auto [x, y] : dp)
(y > maxi)
maxv = x, maxi = y;

<int> inds;
int i = n-1; i >= 0; i--)
(a[i] == maxv)
maxv--, inds.push_back(i+1);

reverse(inds.begin(), inds.end());

<< maxi << endl;
auto i : inds)
cout << i << " ";
