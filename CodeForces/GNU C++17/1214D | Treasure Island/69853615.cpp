#include<bits/stdc++.h>
#define mod 1000000007
#define pb push_back
#define all int i=0; i<n; i++
#define INF 9999999999999999
using namespace std;
typedef long long int ll;
#define int ll
#define FAST_IO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)


int32_t main(){
FAST_IO;
int n,m, ans = 0;
cin>>n>>m;

int arr[n][m];
int reach[n][m];
int reach2[n][m];
int visit[n][m];

for(int i=0; i<n; i++){
for(int j=0; j<m; j++){
reach[i][j] = visit[i][j] = 0;
char k;
cin>>k;
if(k=='.')arr[i][j] = 1;

else arr[i][j] = 0;
}
}

deque<int>q;
deque<int>p;
q.push_back(0);
p.push_back(0);
visit[0][0] = 1;

map<int, int>m1;

while(!q.empty()){
int x = q.front();
int y = p.front();
reach[x][y] = 1;

q.pop_front();
p.pop_front();
if(x+1 < n){
if(arr[x+1][y] == 1 && visit[x+1][y]==0){
visit[x+1][y] = 1;
q.push_back(x+1);
p.push_back(y);
}
}
if(y+1 < m){
if(arr[x][y+1] == 1 && visit[x][y+1]==0){
visit[x][y+1] = 1;
q.push_back(x);
p.push_back(y+1);
}
}
}

if(reach[n-2][m-1] == 1)ans++;
if(reach[n-1][m-2] == 1)ans++;

if(ans<2)cout<<ans<<endl;

else{
for(int i=0; i<n; i++){
for(int j=0; j<m; j++){

reach2[i][j] = visit[i][j] = 0;
}
}
deque<int>q;
deque<int>p;
q.push_back(n-1);
p.push_back(m-1);
visit[n-1][m-1] = 1;
while(!q.empty()){
int x = q.front();
int y = p.front();
visit[x][y] = 1;
reach2[x][y] = 1;
q.pop_front();
p.pop_front();
if(x-1 >= 0 && visit[x-1][y]==0){
if(arr[x-1][y] == 1){
q.push_back(x-1);
p.push_back(y);
visit[x-1][y] = 1;
}
}
if(y-1 >= 0 && visit[x][y-1]==0){
if(arr[x][y-1] == 1){
q.push_back(x);
p.push_back(y-1);
visit[x][y-1] = 1;
}
}
}
reach[0][0] = reach[n-1][m-1] = 0;
ans  = INF;
for(int i=0; i<n; i++){
for(int j=0; j<m; j++){

if(reach[i][j] == 1 &&  reach2[i][j] == 1){
m1[i + j + 1]++;
}
}
}
for(int i=0; i<n; i++){
for(int j=0; j<m; j++){
if(m1[i + j + 1]> 0)
ans = min(ans, m1[i + j + 1]);
}
}

if(ans<2)
cout<<ans<<endl;

else cout<<2<<endl;
}

}