#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef float ff;
typedef vector<long long int> vi;
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define sz(x) (int)x.size()
#define pb(x) push_back(x)
#define endl "\n"

int txtinput(){
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    return 0;
}

int solve(){
    ll n,k;
    cin>>n>>k;
    ll m = 0;
    for (ll i = 1; i <= k; i++)
    {
        m = max(m,n%i);
    }
    cout<<m<<endl;

    return 0;
}


int main(){
    
    txtinput();
    ll t;
    cin>>t;
    
    while(t--){
        solve();
    }
    
    return 0;
}