#include<iostream>
int j(int n,int k){return n>1?(j(n-1,k)+k-1)%n+1:1;}main(){int n;std::cin>>n;std::cout<<j(2020,n+1);}