bits/stdc++.h>
namespace std;

int long long
endl '\n'

BLOCK = 450;
block(val) (val / BLOCK)
value(val) (cnt[val] * cnt[val] * val)


query {
int l, r, idx;


<int> a;
<int> cnt;
<query> qs;


const vector<int> &_a) : a(_a), cnt(*max_element(_a.begin(), _a.end()) + 1) {}

append(const int &l, const int &r) {
.push_back({l, r, (int) qs.size()});


<int> solve() {
sort(qs.begin(), qs.end(), [](query x, query y) {
if (block(x.l) != block(y.l)) return x.l < y.l;
return (block(x.l) & 1) ? (x.r > y.r) : (x.r < y.r);
});

vector<int> ans(qs.size());

int cur = 0;

auto add = [&](const int i) {
cur -= value(a[i]);
cnt[a[i]]++;
cur += value(a[i]);
};

auto del = [&](const int i) {
cur -= value(a[i]);
cnt[a[i]]--;
cur += value(a[i]);
};

for (int l = 0, r = -1, i = 0; i < qs.size(); i++) {
while (l < qs[i].l) del(l++);
while (r < qs[i].r) add(++r);
while (l > qs[i].l) add(--l);
while (r > qs[i].r) del(r--);

ans[qs[i].idx] = cur;
}

return ans;
}
};

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

int n, t; cin >> n >> t;

vector<int> a(n);
for (int i = 0; i < n; i++)
cin >> a[i];

Mo mo(a);
while (t--) {
int l, r; cin >> l >> r;
mo.append(l-1, r-1);
}

for (auto i : mo.solve())
cout << i << endl;
}