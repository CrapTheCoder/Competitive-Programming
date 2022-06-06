bits/stdc++.h>
namespace std;
ll long long int



(ll x,ll y){
0)
return;

s.count(x) && (x>=1 && x<=y)  ){
insert(x);


x/2;
solve(x,y);



{


;
t--){
ll n;
cin>>n;
vector<ll>v(n);
for(int i=0;i<n;i++){
cin>>v[i];

sort(v.begin(), v.end());
for(int i=0;i<n;i++){
solve(v[i],n);

(s.size() == n)
cout << "YES";
else
cout << "NO";
cout<<endl;
s.clear();
}
return 0;

}