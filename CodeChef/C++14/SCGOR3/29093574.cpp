#include<bits/stdc++.h>
using namespace std;
#define o string
#define y INT_MIN
int t(o a,o b,o &e){int f=y;int c=a.length();int d=b.length();for(int i=1;i<=min(c,d);i++){if(!a.compare(c-i,i,b,0,i)){if(f<i){f=i;e=a+b.substr(i);}}}for(int i=1;i<=min(c,d);i++){if(!a.compare(0,i,b,d-i,i)){if(f<i){f=i;e=b+a.substr(i);}}}return f;}
o p(o a[],int e){while(e!=1){int m=y;int l,r;o h;for(int i=0;i<e;i++){for(int j=i+1;j<e;j++){o g;int s=t(a[i],a[j],g);if(m<s){m=s;h=g;l=i,r=j;}}}e--;if(m==y)a[0]+=a[e];else{a[l]=h;a[r]=a[e];}}return a[0];}
int main(){int n;cin>>n;o a[n];for(int i=0;i<n;i++)cin>>a[i];cout<<p(a,n)<<endl;}