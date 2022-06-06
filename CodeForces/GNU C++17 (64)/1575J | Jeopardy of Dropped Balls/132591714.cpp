#include <bits/stdc++.h>
 
using namespace std;
long long a[1005][1005];
void usaco()
{
 freopen("bbreeds.out", "w", stdout) ;
    freopen("bbreeds.in", "r", stdin) ;
}
int main()
{
 //usaco();
 ios_base::sync_with_stdio(0);
 cin.tie(0);
 long long n,m,k;
 cin>>n>>m>>k;
 for(int i=0;i<n;i++)
 {
  for(int j=0;j<m;j++)
  {
   cin>>a[i][j];
  }
 }
 for(int i=0;i<k;i++)
 {
  long long x=0,y=0;
  cin>>y;
  y--;
  while(x<n)
  {
   if(a[x][y]==1)
   {
    a[x][y]=2;
    y++;
   }
   else if(a[x][y]==3)
   {
    a[x][y]=2;
    y--;
   }
   else
   {
    x++;
   }
  }
  cout<<y+1<<" ";
 }
}