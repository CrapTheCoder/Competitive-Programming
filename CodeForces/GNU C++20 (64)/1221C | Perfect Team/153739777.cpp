#include<bits/stdc++.h>
using namespace std; using ll=long long int;
#define tc int t; cin >> t; while(t--)
void solve(){
    int c,m,x;
    cin>>c>>m>>x;
    if(x>=c || x>=m){
        cout<<min(c,m)<<endl;
    }
    else{
        if(max(c-x,m-x)>=2*min(c-x,m-x)){
            cout<<min(c,m)<<endl;
        }
        else{
            cout << x + max(c-x, m-x) / 2 + ((min(c-x, m-x) - max(c-x, m-x) / 2) + max(c-x, m-x) % 2) / 3 << endl;
        }
    }
}
 
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
 
    tc {
        solve();
    }
}