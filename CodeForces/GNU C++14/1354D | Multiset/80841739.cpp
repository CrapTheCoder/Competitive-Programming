#include <bits/stdc++.h>
using namespace std;
 
int n;
int a[1000005];
int tree[1000005];
 
int getsum(int i){
    int s = 0;
    i++;
 
    while(i > 0){
        s += tree[i];
        i -= i & (-i);
    }
 
    return s;
}
 
void updatebit(int i, int v){
    i++;
 
    while(i <= n){
        tree[i] += v;
        i += i & (-i);
    }
}
 
void construct(){
    for(int i = 0; i < n; i++)
        updatebit(i, a[i]);
}
 
int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int q; cin >> n >> q;
 
    for(int i = 0; i < n; i++){
        int k; cin >> k;
        a[k]++;
    }
 
    n++;
 
    construct();
 
    for(int i = 0; i < q; i++){
        int k; cin >> k;
 
        if(k < 0){
            k = -k;
            int l = 0, r = n-1;
 
            while(l < r){
                int m = (l+r) / 2;
                int s = getsum(m);
 
                if(s >= k)
                    r = m;
                else
                    l = m+1;
            }
 
            a[l]--;
            updatebit(l, -1);
        } else {
            a[k]++;
            updatebit(k, 1);
        }
    }
 
    for(int i = 0; i < n; i++){
        if(a[i] >= 1){
            cout << i;
            return 0;
        }
    }
 
    cout << 0;
}