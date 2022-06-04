#include<iostream>
using namespace std;
int j(int n,int k){return n==1?1:((j(n-1,k)+k-1)%n+1);}
int main(){int n;cin>>n;cout<<j(2020,n+1);}