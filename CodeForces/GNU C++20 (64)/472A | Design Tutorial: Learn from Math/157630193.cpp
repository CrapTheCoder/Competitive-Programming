#include <bits/stdc++.h>
using namespace std;
 
#define ll long long int
#define mp make_pair
#define pb push_back
#define tc int t; cin >> t; while(t--)
#define imax INT_MAX
#define imin INT_MIN
#define llmax LLONG_MAX
#define llmin LLONG_MIN
#define nl "\n"
#define pminheap priority_queue<pair<int, int> , vector<pair<int , int>> , greater<pair<int , int>>>
#define minheap priority_queue<int , vector<int> , greater<int>>
#define maxheap priority_queue<int>
#define zeroMatrix vector<vector<int>> v(n , vector<int>(n , 0))
 
bool isPrime(ll &n){
    for(ll i=2 ; i*i <= n ; i++){
        if(n%i ==0){
            return false ;
        }
    }
    return true ;
};
 
int main()
{
    // tc{
        ll n ;
        cin>>n ;
 
        ll a =0 ;
        if(n %2 != 0) a =1 ;
        ll x = n/2 ;
        ll y = x ;
        int cnt =0 ;
        bool flag1 = 1;
        while(flag1){
            y = n/2 + cnt + a;
            flag1 = isPrime(x) || isPrime(y);
            if(flag1){
                x-- ;
                cnt++ ;
            }
        }
 
        cout<<x<<" "<<y<<nl ;
 
    // }
    return 0;
}