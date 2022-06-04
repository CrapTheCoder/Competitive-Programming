//Author: Shivank
#include<bits/stdc++.h>
using namespace std; using ll=long long int;
#define int long long
#define all(x)  (x).begin(),(x).end()
#define tc int t; cin >> t; while(t--)
void solve(){
    int a,b,c; 
    cin>>a>>b>>c; 
    if(a>=c){
        cout<<-1<<" "<<b<<endl;
    }
    else{
        if(min(c,a*b-1)==c){
            cout<<1<<" "<<b<<endl;
        }
        else{
            cout<<1<<" "<<-1<<endl;
        }
    }
}
int32_t main(){
ios_base::sync_with_stdio(0); cin.tie(nullptr);
 
     tc{
         solve();
     }
 
}