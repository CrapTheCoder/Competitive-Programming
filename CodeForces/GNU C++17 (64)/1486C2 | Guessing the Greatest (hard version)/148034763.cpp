bits/stdc++.h>
namespace std;

(int idx) {
<< "! " << idx << endl;


int l, int r) {
<< "? " <<  l << " " << r << endl;
res; cin >> res;
res;


int l, int r, int idx) {
(l < r) {
int mid = (l+r+1) / 2;
int cur = query(mid, idx);

(cur == idx)
l = mid;
else
r = mid-1;


l);


int l, int r, int idx) {
(l < r) {
int mid = (l+r) / 2;
int cur = query(idx, mid);

(cur == idx)
r = mid;
else
l = mid+1;


l);
}

signed main() {
int n; cin >> n;

int idx = query(1, n);

if (idx == 1) {
bs2(idx+1, n, idx);
return 0;
}

if (idx == n) {
bs1(1, idx-1, idx);
return 0;
}

if (idx == query(1, idx))
bs1(1, idx-1, idx);
else
bs2(idx+1, n, idx);
}