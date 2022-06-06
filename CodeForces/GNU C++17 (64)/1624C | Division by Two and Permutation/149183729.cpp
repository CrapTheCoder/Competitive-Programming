#include <bits/stdc++.h>
using namespace std;
#define ll long long int
 
set<ll>s;
 
void solve(ll x,ll y){
    if(x==0)
        return;
 
    if ( !s.count(x) && (x>=1 && x<=y)  ){
        s.insert(x);
    }
    else{
        x=x/2;
        solve(x,y);
    }
}
 
int main() {
 
    int t;
    cin>>t;
    while(t--){
        ll n;
        cin>>n;
        vector<ll>v(n);
        for(int i=0;i<n;i++){
            cin>>v[i];
        }
        sort(v.begin(), v.end());
        for(int i=0;i<n;i++){
            solve(v[i],n);
        }
        if (s.size() == n)
            cout << "YES";
        else
            cout << "NO";
        cout<<endl;
        s.clear();
    }
    return 0;
 
}