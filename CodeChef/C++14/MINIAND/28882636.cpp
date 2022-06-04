#include <iostream>
using namespace std;
#define long long int
int main()
{
 int t;
 cin>>t;
 for(int it=0;it<t;it++)
 {
	 int n;
	 cin>>n;
	 int ar[n];
	 int even[n+1];
	 even[0]=0;
	 for(int i=0;i<n;i++)
	 {
		 cin>>ar[i];
		 if(ar[i]%2==0)
		 even[i+1]=even[i]+1;
		 else
		 even[i+1]=even[i];
	//	cout<<even[i+1]<<endl;
		 }
int q;
cin>>q;
for(int j=0;j<q;j++)
{
	int l;
	int u;
	int flag=0;
	cin>>l>>u;
//	cout<<even[u]<<even[l];

    if(even[u]-even[l-1]==0)
    cout<<"ODD\n";
    else
    cout<<"EVEN\n";
}
}
}
