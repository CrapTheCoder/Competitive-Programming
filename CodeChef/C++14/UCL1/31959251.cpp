/*<----------------------------------------------------------------------->

<-------------------------------------------------------------------------->
            _           __                _      _____ _____ _____ 
  ___ _   _| |__   ___ / _|_ __ ___  __ _| | __ |___  |___  |___  |
 / __| | | | '_ \ / _ \ |_| '__/ _ \/ _` | |/ /    / /   / /   / / 
| (__| |_| | |_) |  __/  _| | |  __/ (_| |   <    / /   / /   / /  
 \___|\__,_|_.__/ \___|_| |_|  \___|\__,_|_|\_\  /_/   /_/   /_/   

*/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll ;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<ll> vi;
typedef vector<pll> vpll;
typedef unordered_map <ll,ll> umap ; 
//#pragma GCC optimize "trapv"
#define loop(i,a,b) for(ll i=a ;i<b;i++)
#define For(i,n) for(int i=0;i<(ll)n;i++)
#define Rev(i,n) for(int i=n-1;i>=0;i--)
#define Rep(i,n) for(int i=1;i<=n;++i)
#define F first
#define S second
#define pb push_back
#define em emplace_back
#define all(v) (v).begin(),(v).end()
#define mems(x, y) memset(x, y, sizeof(x))
#define sz(v) (v).size()
#define mp(a,b) make_pair(a,b)
#define pf(n) cout<<n<<"\n"
#define pff(n) cout << n << " " ; 
#define ar array
long const M=1e9+7;
const long mxN =1e5+2 ;
const long mxNN =1e6+2 ;
ll n ,x;
ar<ll,4> merge(ar<ll,4>A,ar<ll,4>B){
    int cnt_A=0,cnt_B=0 ;
    For(i,3)cnt_A+=(A[i]>B[i]) ;
    For(i,3)cnt_B+=(B[i]>A[i]) ;
    if(cnt_A>=2)return A ;
    if(cnt_B>=2)return B ;
    return A ;
}
struct segtree {
    ar<ll,4>a[1<<18]={} ;
    ll root =1 ;
    void upd(ll index,ar<ll,4> x,ll i=1,ll l2=0,ll r2=n){
        if(l2==r2){
            a[i]=x ;
            return ;
        }
        ll m2 =(l2+r2)/2 ;
        if(index<=m2)
            upd(index,x,2*i,l2,m2);
        else
            upd(index,x,2*i+1,m2+1,r2);
        a[i]=merge(a[2*i],a[2*i+1]) ;
        
    }
    ar<ll,4> qry(ll l1,ll i=1,ll l2=0,ll r2=n){
        if(l2==r2)return a[i] ; 
        ll m2 = (l2+r2)/2 ;
        if(l1<=m2)return qry(l1,2*i,l2,m2);
        else return qry(l1,2*i+1,m2+1,r2) ;
    }
    ll qry1(){
        return a[1][3];
    }
};
void solve(){
    cin >> x ;segtree s ;
    n = 1ll<< x ;
    For(i,n){
        ar<ll,4> f ;
        For(j,3)cin >> f[j] ;
        f[3]=i+1 ;
        s.upd(ll(i+1),f) ;
    }
    ll m ; cin >> m ;
    For(i,m){
        char c;ll z, y ;
        cin >>c>>z >> y ;
        ar<ll,4> Z= s.qry(z) ;
        ar<ll,4> Y=s.qry(y) ;
        Z[3]=y ;Y[3]=z ;
        s.upd(z,Y);s.upd(y,Z) ;
        pf(s.qry1()) ;

    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve() ;
	return 0;
}















