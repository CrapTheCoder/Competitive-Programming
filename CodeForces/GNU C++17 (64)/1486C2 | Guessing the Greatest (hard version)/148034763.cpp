#include <bits/stdc++.h>
using namespace std;
 
void query(int idx) {
    cout << "! " << idx << endl;
}
 
int query(int l, int r) {
    cout << "? " <<  l << " " << r << endl;
    int res; cin >> res;
    return res;
}
 
void bs1(int l, int r, int idx) {
    while (l < r) {
        int mid = (l+r+1) / 2;
        int cur = query(mid, idx);
 
        if (cur == idx)
            l = mid;
        else
            r = mid-1;
    }
 
    query(l);
}
 
void bs2(int l, int r, int idx) {
    while (l < r) {
        int mid = (l+r) / 2;
        int cur = query(idx, mid);
 
        if (cur == idx)
            r = mid;
        else
            l = mid+1;
    }
 
    query(l);
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