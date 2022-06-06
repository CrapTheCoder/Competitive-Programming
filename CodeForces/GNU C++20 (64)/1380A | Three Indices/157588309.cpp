bits/stdc++.h>

namespace std;

ll long long int
mp make_pair
pb push_back
tc int t; cin >> t; while(t--)
imax INT_MAX
imin INT_MIN
llmax LLONG_MAX
llmin LLONG_MIN
nl "\n"
pminheap priority_queue<pair<int, int> , vector<pair<int , int>> , greater<pair<int , int>>>
minheap priority_queue<int , vector<int> , greater<int>>
maxheap priority_queue<int>
zeroMatrix vector<vector<int>> v(n , vector<int>(n , 0))


{

ll n;
cin >> n;

vector<ll> v;
pminheap right;
for (ll i = 0; i < n; i++) {
ll x;
cin >> x;
v.pb(x);
if (i > 1)right.push({x, i});


ll a, b, c;
pminheap left;
left.push({v[0], 0});
bool flag = 0;

(n > 2) {
ll i;
for (i = 1; i < n - 1; i++) {
if (right.top().second == i) {
right.pop();

} else {
if (v[i] > left.top().first && v[i] > right.top().first) {
if (left.top().second < i && i < right.top().second) {
a = left.top().second + 1;
b = i + 1;
c = right.top().second + 1;
flag = 1;
break;
}
}
}

left.push({v[i], i});
}
}

if (!flag) cout << "NO" << nl;
else cout << "YES" << nl << a << " " << b << " " << c << nl;
}
return 0;
}