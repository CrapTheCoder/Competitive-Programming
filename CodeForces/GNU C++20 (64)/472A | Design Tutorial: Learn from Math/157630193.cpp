bits/stdc++.h>
namespace std;

ll long long int
mp make_pair
pb push_back
tc int t; cin >> t; while(t--)
imax INT_MAX
imin INT_MIN
llmax LLONG_MAX
llmin LLONG_MIN
nl "\n"
pminheap priority_queue<pair<int, int> , vector<pair<int , int>> , greater<pair<int , int>>>
minheap priority_queue<int , vector<int> , greater<int>>
maxheap priority_queue<int>
zeroMatrix vector<vector<int>> v(n , vector<int>(n , 0))

isPrime(ll &n){
ll i=2 ; i*i <= n ; i++){
(n%i ==0){
return false ;


true ;





ll n ;
cin>>n ;

ll a =0 ;
(n %2 != 0) a =1 ;
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