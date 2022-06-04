#include<bits/stdc++.h>
using namespace std;
 
const int maxn=207;
int t,d,q;
bool dp[maxn];
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    cin>>t;
    while (t--){
        memset(dp,0,sizeof(dp));
        dp[0]=1;
        cin>>q>>d;
        if (!d) d+=10;
        int mx=d*10;
        for (int i=0;10*i+d<=mx;++i){
            for (int j=0;10*i+d+j<=mx;++j){
                dp[10*i+d+j]|=dp[j];
            }
        }
        while (q--){
            int u;
            cin>>u;
            if (u>=mx||dp[u]) cout<<"YES\n";
            else cout<<"NO\n";
        }
    }
    return 0;
}