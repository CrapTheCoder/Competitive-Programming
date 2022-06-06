bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

typename T>
CoordComp {
sorted = false;
<T> v;

:
add(const T &x) {
push_back(x);


compress() {
sort(v.begin(), v.end());
erase(unique(v.begin(), v.end()), v.end());
sorted = true;


get(const int x) {
(not sorted) assert(false);
return distance(v.begin(), lower_bound(v.begin(), v.end(), x));



SegTree {

<int> tree;

build(int i, int l, int r, const vector<int> &a) {
(l == r) {
tree[i] = a[l];
return;
}

int m = (l + r) / 2;
int lc = i+1, rc = (m-l+1) / 2;

build(lc, l, m, a);
build(rc, m+1, r, a);

tree[i] = unite(tree[lc], tree[rc]);
}

void update(int i, int l, int r, int k, int v) {
if (l == r) {
tree[i] += v;
return;
}

int m = (l + r) / 2;
int lc = i+1, rc = 2 * (m-l+1) + i;

if (k <= m)
update(lc, l, m, k, v);
else
update(rc, m+1, r, k, v);

tree[i] = unite(tree[lc], tree[rc]);
}

int query(int i, int l, int r, int a, int b) {
if (a <= l && r <= b)
return tree[i];

int m = (l + r) / 2;
int lc = i+1, rc = 2 * (m-l+1) + i;

if (b <= m)
return query(lc, l, m, a, b);

if (m < a)
return query(rc, m+1, r, a, b);

return unite(query(lc, l, m, a, b), query(rc, m+1, r, a, b));
}

int unite(int a, int b) {
return a + b;
}

public:
SegTree(int _n) : n(_n), tree(2 * _n) {

}

SegTree(vector<int> a) : n(a.size()), tree(2 * a.size()) {
build(0, 0, n-1, a);
}

void update(int k, int v) {
update(0, 0, n-1, k, v);
}

int query(int a, int b) {
return query(0, 0, n-1, a, b);
}
};

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

int n; cin >> n;
vector<int> a(n);

CoordComp<int> cc;
for (int i = 0; i < n; i++) {
cin >> a[i]; cc.add(a[i]);
}

cc.compress();

int ans = 0;

SegTree left(n), right(n);
for (auto i : a)
right.update(cc.get(i), 1);

for (int i = 0; i < n; i++) {
right.update(cc.get(a[i]), -1);
ans += left.query(cc.get(a[i]), n-1) * right.query(0, cc.get(a[i]));
left.update(cc.get(a[i]), 1);
}

cout << ans << endl;
}